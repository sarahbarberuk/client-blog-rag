from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import os
import re
import time

from scraper_config import SCRAPER_CONFIGS


def scrape_blog_with_playwright(config):
    print(f"[INFO] Launching browser for: {config['url']}")
    with sync_playwright() as p:
        headless = not config.get('force_headed', False)
        browser = p.chromium.launch(headless=headless)
        page = browser.new_page()

        wait_until = config.get("wait_until", "networkidle")
        page.goto(config['url'], wait_until=wait_until, timeout=60000)

        try:
            cookie_button = page.locator('#onetrust-accept-btn-handler')
            cookie_button.wait_for(timeout=5000)
            if cookie_button.is_visible():
                print("[INFO] Accepting cookie consent...")
                cookie_button.click(force=True)
                page.wait_for_timeout(2000)
        except Exception as e:
            print(f"[WARN] Could not click cookie consent button: {e}")

        selector = config.get('load_more_selector')
        if selector:
            while True:
                try:
                    button = page.locator(selector)
                    if button.is_visible() and button.is_enabled():
                        print("[INFO] Clicking 'Load more'...")
                        button.click()
                        page.wait_for_timeout(config.get('load_more_delay', 2000))
                    else:
                        print("[INFO] Button not visible or not enabled, breaking.")
                        break
                except Exception as e:
                    print(f"[ERROR] Exception during 'load more': {e}")
                    break
        else:
            print("[INFO] There is no load more selector")

        page.wait_for_timeout(1000)
        html = page.content()
        browser.close()
        return html


def parse_blog_html(html, config, client_name):
    soup = BeautifulSoup(html, 'html.parser')
    posts = []

    for i, post in enumerate(soup.select(config['post_selector']), start=1):
        title_tag = _first_match(post, config.get('title_selectors') or config.get('title_selector'))
        date_tag  = _first_match(post, config.get('date_selectors')  or config.get('date_selector'))
        author_tag = _first_match(post, config.get('author_selectors') or config.get('author_selector'))

        title = title_tag.get_text(strip=True) if title_tag else 'Untitled'
        date  = date_tag.get_text(strip=True)  if date_tag  else ''
        author = author_tag.get_text(strip=True) if author_tag else ''

        link_tag = post.select_one("a") if post.name != "a" else post
        href = link_tag.get("href", "") if link_tag else post.get("href", "")
        link = f"{config['base_url']}{href}" if href.startswith('/') else href

        posts.append((title, link, date, author, client_name))
        print(f"[DEBUG] ({client_name}) Post {i}: Title='{title}', URL='{link}', Date='{date}', Author='{author}'")

    print(f"[INFO] ({client_name}) Found {len(posts)} posts")
    return posts


def fetch_article_content(page, url, config):
    """
    Fetch the full text content of a single article page.
    Accepts an already-open Playwright page object to avoid
    launching a new browser for every article.
    """
    try:
        page.goto(url, wait_until="domcontentloaded", timeout=60000)
        html = page.content()
        soup = BeautifulSoup(html, "html.parser")

        title_tag = soup.select_one("h1")
        title = title_tag.get_text(strip=True) if title_tag else "Untitled"

        body_tag = soup.select_one(config["article_body_selector"])
        if not body_tag:
            print(f"[WARN] No article body found at {url} - skipping")
            return None

        body = body_tag.get_text(separator="\n", strip=True)

        return {"title": title, "url": url, "body": body}

    except Exception as e:
        print(f"[ERROR] Failed to fetch {url}: {e}")
        return None


def slugify(text):
    """Convert a title to a safe filename."""
    text = text.lower()
    text = re.sub(r'[^a-z0-9]+', '-', text)
    text = text.strip('-')
    return text[:80]  # cap length to avoid overly long filenames


def save_article_as_markdown(article, output_dir):
    """
    Save a fetched article as a markdown file with frontmatter
    containing the title, url, and date for use during ingestion.
    """
    os.makedirs(output_dir, exist_ok=True)

    slug = slugify(article["title"])
    filepath = os.path.join(output_dir, f"{slug}.md")

    with open(filepath, "w", encoding="utf-8") as f:
        f.write("---\n")
        f.write(f"title: {article['title']}\n")
        f.write(f"url: {article['url']}\n")
        f.write("---\n\n")
        f.write(article["body"])

    print(f"[INFO] Saved: {filepath}")
    return filepath


def _first_match(post, selectors):
    if not selectors:
        return None
    if isinstance(selectors, str):
        selectors = [selectors]
    for sel in selectors:
        if not sel:
            continue
        node = post.select_one(sel)
        if node:
            return node
    return None


def main():
    all_posts = []

    # Step 1: Scrape the blog index to get all article URLs
    for client_name, config in SCRAPER_CONFIGS.items():
        print(f"\n[INFO] Scraping blog index for: {client_name}")
        html = scrape_blog_with_playwright(config)

        if 'display_name' not in config:
            raise KeyError(f"[ERROR] 'display_name' is missing in config for client: {client_name}")

        posts = parse_blog_html(html, config, config['display_name'])
        all_posts.extend(posts)

    if not all_posts:
        print("[WARN] No posts found.")
        return

    # Step 2: Fetch full article content for each URL and save as markdown
    # Articles already saved to disk are skipped so the script can be
    # safely stopped and restarted without re-scraping everything.
    print(f"\n[INFO] Fetching full article content for {len(all_posts)} articles...")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Handle cookie consent once on the first page
        first_url = all_posts[0][1]
        page.goto(first_url, wait_until="domcontentloaded", timeout=60000)
        try:
            cookie_button = page.locator('#onetrust-accept-btn-handler')
            cookie_button.wait_for(timeout=5000)
            if cookie_button.is_visible():
                print("[INFO] Accepting cookie consent...")
                cookie_button.click(force=True)
                page.wait_for_timeout(2000)
        except Exception:
            pass

        for i, post in enumerate(all_posts):
            title, url, date, author, client = post
            articles_dir = f"data/articles/{client.lower()}"
            slug = slugify(title)
            filepath = os.path.join(articles_dir, f"{slug}.md")

            if os.path.exists(filepath):
                print(f"[INFO] Skipping (already scraped): {title}")
                continue

            print(f"\n[INFO] ({i+1}/{len(all_posts)}) {title}")

            client_config = SCRAPER_CONFIGS[client.lower()]
            article = fetch_article_content(page, url, client_config)
            
            if article:
                save_article_as_markdown(article, articles_dir)

            time.sleep(2)  # rate limiting — 2 seconds between requests

        browser.close()

    print(f"\n[INFO] Done.")


if __name__ == '__main__':
    main()
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import os
import re
import time

from scraper_config import SCRAPER_CONFIGS


def get_all_article_urls(page, config):
    """
    Fetch all blog article URLs from the client's sitemap page.
    Filters out author, category, and tag pages leaving only article URLs.
    """
    sitemap_url = config["sitemap_url"]
    base_url = config["base_url"]
    print(f"[INFO] Fetching article URLs from: {sitemap_url}")

    page.goto(sitemap_url, wait_until="domcontentloaded", timeout=60000)
    html = page.content()

    soup = BeautifulSoup(html, "html.parser")
    urls = []

    for a in soup.select("a[href*='/blog/']"):
        href = a.get("href", "")
        if any(x in href for x in ["/blog/author/", "/blog/category/", "/blog/tag/"]):
            continue
        if href.rstrip("/") in ["/blog", ""]:
            continue
        full_url = f"{base_url}{href}" if href.startswith("/") else href
        if full_url not in urls:
            urls.append(full_url)

    print(f"[INFO] Found {len(urls)} article URLs")
    return urls


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
    """Convert a title or URL slug to a safe filename."""
    text = text.lower()
    text = re.sub(r'[^a-z0-9]+', '-', text)
    text = text.strip('-')
    return text[:80]


def save_article_as_markdown(article, output_dir):
    """
    Save a fetched article as a markdown file with frontmatter
    containing the title and url for use during ingestion.
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


def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        for client_name, config in SCRAPER_CONFIGS.items():
            print(f"\n[INFO] Processing client: {client_name}")
            articles_dir = f"data/articles/{config['display_name'].lower()}"

            # Step 1: Get all article URLs from the sitemap
            urls = get_all_article_urls(page, config)

            if not urls:
                print(f"[WARN] No URLs found for {client_name}")
                continue

            print(f"\n[INFO] Fetching full article content for {len(urls)} articles...")

            # Handle cookie consent once on the first page
            page.goto(urls[0], wait_until="domcontentloaded", timeout=60000)
            try:
                cookie_button = page.locator('#onetrust-accept-btn-handler')
                cookie_button.wait_for(timeout=5000)
                if cookie_button.is_visible():
                    print("[INFO] Accepting cookie consent...")
                    cookie_button.click(force=True)
                    page.wait_for_timeout(2000)
            except Exception:
                pass

            # Step 2: Fetch full article content for each URL and save as markdown.
            # Articles already saved to disk are skipped so the script can be
            # safely stopped and restarted without re-scraping everything.
            for i, url in enumerate(urls):
                url_slug = url.rstrip("/").split("/")[-1]
                slug = slugify(url_slug)
                filepath = os.path.join(articles_dir, f"{slug}.md")

                if os.path.exists(filepath):
                    print(f"[INFO] Skipping (already scraped): {url}")
                    continue

                print(f"\n[INFO] ({i+1}/{len(urls)}) {url}")

                article = fetch_article_content(page, url, config)
                if article:
                    save_article_as_markdown(article, articles_dir)

                time.sleep(2)  # rate limiting — 2 seconds between requests

        browser.close()

    print(f"\n[INFO] Done.")


if __name__ == '__main__':
    main()
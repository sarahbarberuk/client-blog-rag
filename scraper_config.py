# Configuration for each client. E.g. what URL to be scraped, how to identify titles, dates etc.
SCRAPER_CONFIGS = {
    "contentful": {
        "display_name": "Contentful",
        "url": "https://www.contentful.com/blog/category/guides/",
        "article_body_selector": 'main',
        "post_selector": 'a[class*="blog_entry_card_card"]',
        "title_selector": 'p[class*="card_with_image_title"]',
        "date_selector": 'p[class*="card_with_image_description"]',
        "base_url": "https://www.contentful.com",
        "needs_click_to_load_more": True,
        "load_more_selector": 'button:has-text("See more articles")',
        "load_more_delay": 2000,
        "wait_until": "domcontentloaded"

    },
    # "appsmith": {
    #     "display_name": "Appsmith",
    #     "url": "https://www.appsmith.com/blog",
    #     "post_selector": "a[href^='/blog/']",
    #     "title_selectors": [
    #         "h2.leading-tight span",                               
    #         "span.text-base.font-medium.leading-tight"  
    #     ],
    #     "date_selectors": [
    #         "h2.font-display ~ div time", 
    #         "div.text-xs.text-primary-light-500\\/70"
    #     ],
    #     "author_selectors": [
    #         "h2.font-display ~ div .text-ellipsis.text-sm.font-medium",
    #         "div.text-ellipsis.text-sm.font-medium"
    #     ],
    #     "base_url": "https://www.appsmith.com",
    #     "needs_click_to_load_more": True,
    #     "load_more_selector": 'button:has-text("Load more")',
    #     "load_more_delay": 2000,
    #     "wait_until": "domcontentloaded"
    # },
    # "stytch": {
    #     "display_name": "Stytch",
    #     "url": "https://stytch.com/blog/category/latest/",
    #     "post_selector": "main > section:first-of-type a[href^='/blog/']:has(h3)",
    #     "title_selector": "main > section:first-of-type a[href^='/blog/'] h3",
    #     "date_selector": "main > section:first-of-type a[href^='/blog/'] p",
    #     "base_url": "https://www.stytch.com",
    #     "needs_click_to_load_more": False,
    #     "wait_until": "domcontentloaded"
    # },
    #     "akamai": {
    #     "display_name": "Akamai",
    #     "url": "https://akamai.com/blog/",
    #     "post_selector": "div.card.post", 
    #     "title_selector": "h3 > a",        
    #     "date_selector": "div.post__author",
    #     "author_selector": "div.post__author > [href^='/blog?author=']",
    #     "base_url": "https://www.akamai.com",
    #     "needs_click_to_load_more": True,
    #     "load_more_selector": 'div.filter-items__load-more a[rel="next"]',
    #     "load_more_delay": 3000,
    #     "wait_until": "domcontentloaded",
    #     "force_headed": True  
    # }
}
import requests
import logging
from bs4 import BeautifulSoup
from typing import Dict, List, Optional
from playwright.sync_api import sync_playwright
import re
# --------------------------------------------------
# Logging configuration
# --------------------------------------------------
logger = logging.getLogger(__name__)

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36",
    "Accept-Language": "en-IN,en;q=0.9"
}

TIMEOUT = 10


# --------------------------------------------------
# Utility: Safe HTTP GET
# --------------------------------------------------
def fetch_page(url: str) -> Optional[str]:
    try:
        response = requests.get(url, headers=HEADERS, timeout=TIMEOUT)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        logging.error(f"Failed to fetch {url} | Error: {e}")
        return None


# --------------------------------------------------
# Amazon Scraper
# --------------------------------------------------
def scrape_amazon(product_name: str):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        search_url = f"https://www.amazon.in/s?k={product_name.replace(' ', '+')}"
        page.goto(search_url, timeout=60000)

        page.wait_for_selector("span.a-price-whole", timeout=10000)

        price_text = page.locator("span.a-price-whole").first.inner_text()

        browser.close()

        return {
            "source": "Amazon",
            "price": f"₹{price_text}",
            "url": search_url,
            "status": "success"
        }


# --------------------------------------------------
# Flipkart Scraper
# --------------------------------------------------
def scrape_bigbasket(product_name: str):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        search_url = f"https://www.bigbasket.com/ps/?q={product_name.replace(' ', '%20')}"
        page.goto(search_url, timeout=60000)

        page.wait_for_selector("span.Pricestyles__PriceText-sc-1xmk48x-0", timeout=15000)

        price_text = page.locator(
            "span.Pricestyles__PriceText-sc-1xmk48x-0"
        ).first.inner_text()

        browser.close()

        return {
            "source": "BigBasket",
            "price": price_text,
            "url": search_url,
            "status": "success"
        }

# --------------------------------------------------
# Croma Scraper
# --------------------------------------------------
def scrape_croma(product_name: str):
    url = f"https://www.croma.com/search/?text={product_name.replace(' ', '%20')}"

    try:
        r = requests.get(url, headers=HEADERS, timeout=10)
        r.raise_for_status()

        soup = BeautifulSoup(r.text, "html.parser")
        price = soup.select_one("span.amount")

        if not price:
            return None

        return {
            "source": "Croma",
            "price": price.text.strip(),
            "url": url
        }

    except Exception as e:
        logger.error(f"Croma scrape failed: {e}")
        return None

def scrape_flipkart(product_name: str):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        search_url = f"https://www.flipkart.com/search?q={product_name.replace(' ', '%20')}"
        page.goto(search_url, timeout=60000)

        # Close login popup if it appears
        try:
            page.locator("button._2KpZ6l._2doB4z").click(timeout=3000)
        except:
            pass

        page.wait_for_selector("div._30jeq3", timeout=10000)

        price_text = page.locator("div._30jeq3").first.inner_text()

        browser.close()

        return {
            "source": "Flipkart",
            "price": price_text,
            "url": search_url,
            "status": "success"
        }

# --------------------------------------------------
# Aggregator
# --------------------------------------------------
def scrape_all(product_name: str):
    results = []

    for scraper in [scrape_amazon, scrape_flipkart, scrape_bigbasket]:
        try:
            results.append(scraper(product_name))
        except Exception as e:
            results.append({
                "source": scraper.__name__.replace("scrape_", "").title(),
                "status": "error",
                "error": str(e)
            })

    return results

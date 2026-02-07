from fastapi import FastAPI
from scraper import scrape_all
from normalization import normalize_price
from comparator import compare_prices
from models import ProductRequest

app = FastAPI(title="Product Price Comparison API")

OUR_INTERNAL_PRICE = 60000  # Example internal price


@app.post("/compare-price")
def compare_price(product: ProductRequest):
    scraped = scrape_all(product.product_name)
    print("SCRAPED:", scraped)

    enriched = []

    for item in scraped:
        if item.get("status") == "success" and item.get("price"):
            normalized = normalize_price(item["price"])

            if normalized:
                enriched.append({
                    "source": item.get("source"),
                    "raw_price": item.get("price"),
                    "price": normalized,
                    "url": item.get("url"),
                    "status": "success"
                })
        else:
            # ✅ Preserve failed sources for transparency
            enriched.append({
                "source": item.get("source"),
                "raw_price": item.get("raw_price"),
                "price": None,
                "url": item.get("url"),
                "status": item.get("status", "failed"),
                "error": item.get("error")
            })

    result = compare_prices(enriched)

    return {
        "product": product.product_name,
        "result": result
    }

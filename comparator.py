from typing import List, Dict, Optional


def compare_prices(data, threshold=0.1):
    valid = [item for item in data if item.get("price")]

    if len(valid) < 2:
        return {
            "min_price": valid[0]["price"]["amount"] if valid else None,
            "max_price": valid[0]["price"]["amount"] if valid else None,
            "alert": False,
            "reason": "Insufficient competitor data",
            "data": valid
        }


    if not valid:
        return {
            "min_price": None,
            "max_price": None,
            "alert": False,
            "data": []
        }

    prices = [item["price"]["amount"] for item in valid]

    min_price = min(prices)
    max_price = max(prices)

    alert = (max_price - min_price) / min_price > threshold if min_price else False

    return {
        "min_price": min_price,
        "max_price": max_price,
        "alert": alert,
        "data": valid
    }

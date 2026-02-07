import re

def normalize_price(raw_price):
    if not raw_price:
        return None

    # Convert to string
    raw_price = str(raw_price)

    # Remove currency symbols, commas, spaces
    cleaned = re.sub(r"[^\d.]", "", raw_price)

    try:
        amount = float(cleaned)
        return {
            "amount": int(amount),
            "currency": "INR"
        }
    except:
        return None

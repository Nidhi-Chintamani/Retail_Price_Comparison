# Retail Price Comparison API

A **production-ready FastAPI application** for real-time product price comparison across multiple e-commerce platforms like **Amazon, Flipkart, and BigBasket**. It supports web scraping, price normalization, competitor comparison, and alerting. Designed to be extendable with **ML and GenAI features**.

---

## 🏗 Project Structure

Retail_Price_Comparison/
│
├── main.py # FastAPI application entrypoint
├── scraper.py # Web scraping logic for Amazon, Flipkart, BigBasket
├── normalization.py # Price normalization logic
├── comparator.py # Compare prices & generate alerts
├── models.py # Pydantic request/response models
├── requirements.txt # Python dependencies
├── .gitignore # Ignored files (env, cache, logs)
└── README.md # Project documentation

---

## ⚙️ Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/Retail_Price_Comparison.git
cd Retail_Price_Comparison
Create a virtual environment and activate it:

2. Create a virtual environment and activate it:
python3 -m venv myenv
source myenv/bin/activate
Install dependencies:

3.Install dependencies:
pip install -r requirements.txt
Install Playwright browsers (required for scraping):

4. Install Playwright browsers (required for scraping):
python -m playwright install

🚀 Running the API
Start the FastAPI server:

uvicorn main:app --reload
Open Swagger UI at:

http://127.0.0.1:8000/docs

📦 API Endpoint
POST /compare-price
Request:


{
  "product_name": "Maggi 2 Minute Noodles 560g"
}
Response:
{
  "product": "Maggi 2 Minute Noodles 560g",
  "result": {
    "min_price": 92,
    "max_price": 135,
    "alert": true,
    "reason": "Internal price differs from competitors",
    "data": [
      {
        "source": "Amazon",
        "raw_price": "₹135",
        "price": {
          "amount": 135,
          "currency": "INR"
        },
        "url": "https://www.amazon.in/s?k=Maggi+2+Minute+Noodles+560g",
        "status": "success"
      },
      {
        "source": "BigBasket",
        "raw_price": "₹92",
        "price": {
          "amount": 92,
          "currency": "INR"
        },
        "url": "https://www.bigbasket.com/...",
        "status": "success"
      }
    ]
  }
}
min_price / max_price: computed from competitor prices

alert: true if your internal price differs significantly

reason: explanation for alert or insufficient data

🛠 Features

Real-time scraping of Amazon, Flipkart, BigBasket

Price normalization for consistent comparison

Competitor price comparison & alert generation

Modular design to add ML/GenAI features later

Transparent handling of failed scrapes

Notes

Ensure Playwright browsers are installed before running.

Currently supports Amazon, Flipkart, and BigBasket; more sources can be added.

.gitignore excludes virtual environment, cache, logs, and browser binaries.

Author

Nidhi Chintamani
LinkedIn: https://www.linkedin.com/in/nidhichintamani

GitHub: https://github.com/Nidhi-Chintamani


Retail Price Comparison API

A FastAPI-based Python project that provides competitive pricing intelligence by scraping product prices from multiple e-commerce platforms (Amazon, Flipkart, BigBasket), normalizing them, and generating threshold-based alerts.

🏗 Project Structure
Retail_Price_Comparison/
├── main.py           # FastAPI application entrypoint
├── scraper.py        # Web scraping logic for Amazon, Flipkart, BigBasket
├── normalization.py  # Price normalization logic
├── comparator.py     # Compare prices & generate alerts
├── models.py         # Pydantic request/response models
├── requirements.txt  # Python dependencies
├── .gitignore        # Ignored files (env, cache, logs)
└── README.md         # Project documentation

⚡ Features

Real-time web scraping of multiple e-commerce websites

Price normalization and currency handling

Min/max price comparison against internal prices

Threshold-based alerts for price changes

Clear structured JSON API response

Modular design for adding more platforms easily

🚀 Installation
# Clone the repository
git clone https://github.com/<your-username>/Retail_Price_Comparison.git
cd Retail_Price_Comparison

# Create and activate virtual environment
python3 -m venv myenv
source myenv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Install Playwright browsers for scraping
python -m playwright install

🏃‍♂️ Running the API
uvicorn main:app --reload


Open Swagger UI at: http://127.0.0.1:8000/docs

Example POST request to /compare-price:

{
  "product_name": "Maggi 2 Minute Noodles 560g"
}

📦 Sample Response
{
  "product": "Maggi 2 Minute Noodles 560g",
  "result": {
    "min_price": 135,
    "max_price": 135,
    "alert": false,
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
      }
    ]
  }
}
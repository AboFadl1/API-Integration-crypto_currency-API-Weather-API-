# API Integration Demo (Python)

This repository contains two beginner-friendly examples of how to integrate with public APIs in Python.

- **`crypto_price.py`** → fetches the latest price of a cryptocurrency (Bitcoin, Ethereum, etc.) using the [CoinGecko API](https://www.coingecko.com/en/api).
- **`weather.py`** → fetches the current weather for any city using the [Open-Meteo API](https://open-meteo.com/).

Both APIs are free and require **no API key**.

---

## 📦 Requirements

- Python **3.10+**
- `requests` library

Install dependencies:

pip install -r requirements.txt

python -m venv .venv
# On Windows (PowerShell):
.\.venv\Scripts\Activate
# On macOS/Linux:
source .venv/bin/activate

Run These Scripts:
python crypto_price.py --coin bitcoin (for example) --currency usd (for example)
And
python weather.py --city "Cairo" (for example)

api-integration-demo/
│── crypto_price.py   # Get cryptocurrency prices
│── weather.py        # Get city weather
│── utils.py          # Helper functions (API calls, printing, error handling)
│── utils_explained.txt  # Python dependencies and explanation for code
│── README.md         # This file



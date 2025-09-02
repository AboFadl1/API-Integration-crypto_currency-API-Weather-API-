    # crypto_price.py
import argparse
from utils import get_json, print_kv, APIError

API = "https://api.coingecko.com/api/v3/simple/price"

def main():
    p = argparse.ArgumentParser(description="Fetch spot price for a crypto coin.")
    p.add_argument("--coin", default="bitcoin", help="e.g., bitcoin, ethereum")
    p.add_argument("--currency", default="usd", help="e.g., usd, eur, egp")
    args = p.parse_args()

    try:
        data = get_json(API, params={"ids": args.coin, "vs_currencies": args.currency})
        if args.coin not in data or args.currency not in data[args.coin]:
            raise APIError(f"Unexpected response: {data}")
        price = data[args.coin][args.currency]
        print_kv("Crypto Price", {"coin": args.coin, "currency": args.currency, "price": price})
    except APIError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

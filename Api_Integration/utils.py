# utils.py
import requests

# default timeout (in seconds) for all API calls
DEFAULT_TIMEOUT = 10  

# custom exception type for our API errors
class APIError(Exception):
    pass


def get_json(url: str, params: dict | None = None):
    """
    Perform a GET request and return the response as JSON.
    
    - url: the API endpoint (string)
    - params: query parameters (dict), e.g. {"ids": "bitcoin", "vs_currencies": "usd"}
    
    This function:
      1. Makes the request with a timeout
      2. Handles network errors
      3. Checks HTTP status codes
      4. Parses JSON and raises a clean error if invalid
    """
    try:
        # send GET request
        r = requests.get(url, params=params, timeout=DEFAULT_TIMEOUT)
    except requests.RequestException as e:
        # any network problem (no internet, DNS fail, etc.)
        raise APIError(f"Network error: {e}") from e

    if not r.ok:
        # if HTTP status is not 200 (OK)
        msg = r.text.strip()  # the body of the error response
        # keep message short if it's very long
        snippet = (msg[:200] + "...") if len(msg) > 200 else msg
        raise APIError(f"HTTP {r.status_code} from {url}: {snippet}")

    try:
        # try converting response to JSON
        return r.json()
    except ValueError as e:
        # if response was not JSON (e.g. plain text)
        raise APIError("Response was not valid JSON") from e


def print_kv(title: str, data: dict):
    """
    Pretty-print key/value pairs in a simple table format.
    
    Example:
    === Crypto Price ===
    coin     : bitcoin
    currency : usd
    price    : 20000
    """
    print(f"\n=== {title} ===")
    # calculate width for alignment (longest key)
    width = max(len(k) for k in data.keys())
    # print each key and value aligned
    for k, v in data.items():
        print(f"{k:<{width}} : {v}")
        
        
#    python crypto_price.py --coin bitcoin --currency usd
#    python weather.py --city "Cairo"

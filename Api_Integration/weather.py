# weather.py
from utils import get_json, print_kv, APIError
import argparse

GEOCODE = "https://geocoding-api.open-meteo.com/v1/search"
WEATHER = "https://api.open-meteo.com/v1/forecast"

def geocode_city(city: str):
    res = get_json(GEOCODE, params={"name": city, "count": 1, "language": "en", "format": "json"})
    results = res.get("results") or []
    if not results:
        raise APIError(f"City '{city}' not found")
    top = results[0]
    return top["latitude"], top["longitude"], top.get("country"), top.get("admin1")

def main():
    p = argparse.ArgumentParser(description="Current weather for a city.")
    p.add_argument("--city", required=True, help="e.g., Cairo, Paris, Nairobi")
    args = p.parse_args()

    try:
        lat, lon, country, admin = geocode_city(args.city)
        params = {
            "latitude": lat,
            "longitude": lon,
            "current_weather": True,
            "hourly": "temperature_2m,relative_humidity_2m,precipitation",
            "forecast_days": 1,
        }
        data = get_json(WEATHER, params=params)
        current = data.get("current_weather") or {}
        info = {
            "city": args.city,
            "country": country or "",
            "region": admin or "",
            "temp_C": current.get("temperature"),
            "windspeed_kmh": current.get("windspeed"),
            "conditions_code": current.get("weathercode"),
            "time": current.get("time"),
        }
        print_kv("Current Weather", info)
    except APIError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

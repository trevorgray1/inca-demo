# fetch.py: Extract data from blockchain APIs
#
# This function fetches the current Bitcoin price from the CoinGecko API.
# CoinGecko is a free, public API for cryptocurrency data (no API key required).
# Docs: https://www.coingecko.com/en/api/documentation

import requests

def fetch_data():
    """
    Fetch current Bitcoin price data from CoinGecko.
    Returns:
        dict: JSON response with price and market data.
    """
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": "bitcoin",
        "vs_currencies": "usd",
        "include_market_cap": "true",
        "include_24hr_vol": "true",
        "include_24hr_change": "true"
    }
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()  # Raises error for bad HTTP status
        data = response.json()
        # Example output: {'bitcoin': {'usd': 43000, 'usd_market_cap': ..., ...}}
        return data
    except requests.RequestException as e:
        print(f"Error fetching data from CoinGecko: {e}")
        return None

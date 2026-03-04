# process.py: Transform/clean blockchain data

def process_data(raw_data):
    """
    Extract and structure relevant fields from CoinGecko API response.
    Args:
        raw_data (dict): Raw API response from fetch_data().
    Returns:
        dict: Processed data with selected fields, or None if input is invalid.
    """
    # Example CoinGecko response:
    # {'bitcoin': {'usd': 43000, 'usd_market_cap': ..., 'usd_24h_vol': ..., 'usd_24h_change': ...}}
    if not raw_data or 'bitcoin' not in raw_data:
        print("No bitcoin data found in API response.")
        return None
    btc = raw_data['bitcoin']
    processed = {
        'symbol': 'BTC',
        'price_usd': btc.get('usd'),
        'market_cap_usd': btc.get('usd_market_cap'),
        'volume_24h_usd': btc.get('usd_24hr_vol') or btc.get('usd_24h_vol'),  # handle both spellings
        'change_24h_pct': btc.get('usd_24hr_change') or btc.get('usd_24h_change'),
    }
    print("Processed data:", processed)  # For learning/verification
    return processed

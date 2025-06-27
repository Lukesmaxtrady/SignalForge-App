import requests

def get_coinglass_funding(symbol="BTCUSDT"):
    # You need an API key (register for one at CoinGlass)
    key = "YOUR_COINGLASS_API_KEY"
    url = f"https://open-api.coinglass.com/api/pro/v1/futures/funding_rates?symbol={symbol}"
    headers = {"coinglassSecret": key}
    resp = requests.get(url, headers=headers)
    if resp.status_code == 200:
        return resp.json()
    return None
import requests

def get_coingecko_price(symbol_id="bitcoin"):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={symbol_id}&vs_currencies=usd"
    resp = requests.get(url)
    if resp.status_code == 200:
        return resp.json()
    return None
import requests

class KaikoSignal:
    def __init__(self, api_key):
        self.api_key = api_key

    def fetch_data(self, symbol, data_type="ohlcv"):
        url = f"https://us.market-api.kaiko.io/v1/data/trades.v1/spot_exchange_rate/{symbol}/usd"
        headers = {"X-Api-Key": self.api_key}
        try:
            resp = requests.get(url, headers=headers, timeout=5)
            return resp.json()
        except Exception as e:
            return {"error": str(e)}

    def status(self):
        return {"integration": "Kaiko", "status": "ready"}

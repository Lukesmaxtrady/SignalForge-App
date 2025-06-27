import requests

class CoinStatsSignal:
    def __init__(self, api_key):
        self.api_key = api_key

    def get_market_data(self, symbol):
        url = f"https://api.coinstats.app/public/v1/coins/{symbol}"
        headers = {"X-API-KEY": self.api_key}
        try:
            resp = requests.get(url, headers=headers, timeout=5)
            return resp.json()
        except Exception as e:
            return {"error": str(e)}

    def status(self):
        return {"integration": "CoinStats", "status": "ready"}

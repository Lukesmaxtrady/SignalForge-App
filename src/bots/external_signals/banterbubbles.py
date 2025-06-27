import requests

class BanterBubblesSignal:
    def __init__(self, api_url):
        self.api_url = api_url

    def fetch_bubbles(self, symbol):
        url = f"{self.api_url}/bubbles/{symbol}"
        try:
            resp = requests.get(url, timeout=5)
            return resp.json()
        except Exception as e:
            return {"error": str(e)}

    def status(self):
        return {"integration": "BanterBubbles", "status": "ready"}

import requests

class OpenBBSignal:
    def __init__(self, api_url):
        self.api_url = api_url

    def fetch_data(self, endpoint, params=None):
        url = f"{self.api_url}/{endpoint}"
        try:
            resp = requests.get(url, params=params, timeout=5)
            return resp.json()
        except Exception as e:
            return {"error": str(e)}

    def status(self):
        return {"integration": "OpenBB", "status": "ready"}

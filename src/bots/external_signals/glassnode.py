import requests

class GlassnodeSignal:
    def __init__(self, api_key):
        self.api_key = api_key

    def fetch_metric(self, asset, metric):
        url = f"https://api.glassnode.com/v1/metrics/{metric}"
        params = {"a": asset, "api_key": self.api_key}
        try:
            resp = requests.get(url, params=params, timeout=5)
            return resp.json()
        except Exception as e:
            return {"error": str(e)}

    def status(self):
        return {"integration": "Glassnode", "status": "ready"}

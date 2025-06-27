import requests

def get_coinstats_portfolio(api_key, portfolio_id):
    url = f"https://api.coin-stats.com/v3/portfolios/{portfolio_id}/balance"
    headers = {"X-API-KEY": api_key}
    resp = requests.get(url, headers=headers)
    if resp.status_code == 200:
        return resp.json()
    return None
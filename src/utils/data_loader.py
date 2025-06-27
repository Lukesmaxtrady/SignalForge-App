import pandas as pd
import requests
import os
import yfinance as yf

def load_ohlcv(symbol, source="local", start=None, end=None, premium=False, fallback_sources=None):
    # 1. Try premium if toggled
    if premium:
        token = os.getenv("PREMIUM_DATA_TOKEN", None)
        if token:
            url = f"https://premium-feed.com/api/ohlcv?symbol={symbol}&start={start}&end={end}&token={token}"
            try:
                df = pd.read_csv(url)
                df["source"] = "premium"
                return df
            except Exception as e:
                print("Premium feed failed:", e)
    # 2. Local file
    local_path = f"data/ohlcv/{symbol}.csv"
    if os.path.exists(local_path):
        df = pd.read_csv(local_path)
        df["source"] = "local"
        return df
    # 3. Free APIs fallback
    if fallback_sources is None:
        fallback_sources = ["coingecko", "yahoo"]
    for src in fallback_sources:
        try:
            if src == "coingecko":
                resp = requests.get(f"https://api.coingecko.com/api/v3/coins/{symbol}/market_chart?vs_currency=usd&days=max")
                if resp.status_code == 200:
                    j = resp.json()
                    df = pd.DataFrame(j["prices"], columns=["timestamp", "close"])
                    df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ms")
                    df["source"] = "coingecko"
                    return df
            elif src == "yahoo":
                data = yf.download(symbol, start=start, end=end)
                data["source"] = "yahoo"
                return data
        except Exception as e:
            print(f"{src} fallback failed:", e)
    raise FileNotFoundError(f"No OHLCV found for {symbol} in any source!")

def save_ohlcv(df, symbol):
    os.makedirs("data/ohlcv", exist_ok=True)
    df.to_csv(f"data/ohlcv/{symbol}.csv", index=False)
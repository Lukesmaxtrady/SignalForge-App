import ccxt
import os

def get_blofin_client(demo=True):
    key = os.getenv("BLOFIN_API_KEY")
    secret = os.getenv("BLOFIN_API_SECRET")
    params = {"apiKey": key, "secret": secret}
    exchange = ccxt.blofin(params)
    if demo:
        exchange.set_sandbox_mode(True)
    return exchange

def get_balance(client):
    return client.fetch_balance()

def create_order(client, symbol, side, size, price=None, type="market"):
    return client.create_order(symbol=symbol, type=type, side=side, amount=size, price=price)
import ccxt
import os

def get_bitget_client(demo=True):
    key = os.getenv("BITGET_API_KEY")
    secret = os.getenv("BITGET_API_SECRET")
    password = os.getenv("BITGET_API_PASSWORD", "")
    params = {"apiKey": key, "secret": secret}
    if password:
        params["password"] = password
    exchange = ccxt.bitget(params)
    if demo:
        exchange.set_sandbox_mode(True)
    return exchange

def get_balance(client):
    return client.fetch_balance()

def create_order(client, symbol, side, size, price=None, type="market"):
    return client.create_order(symbol=symbol, type=type, side=side, amount=size, price=price)
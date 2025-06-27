def get_tradingview_widget(symbol="BINANCE:BTCUSDT", interval="1H"):
    url = f"https://www.tradingview.com/widgetembed/?frameElementId=tradingview_c4e09&symbol={symbol}&interval={interval}&hidesidetoolbar=1&hidetoptoolbar=1"
    return url

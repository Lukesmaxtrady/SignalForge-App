import pandas as pd
from ta.momentum import RSIIndicator
from ta.trend import MACD

class RSIMACDBot:
    def __init__(self, rsi_period=14, macd_fast=12, macd_slow=26, macd_signal=9):
        self.rsi_period = rsi_period
        self.macd_fast = macd_fast
        self.macd_slow = macd_slow
        self.macd_signal = macd_signal

    def predict(self, data: pd.DataFrame):
        close = data['close']

        # Calculate RSI
        rsi = RSIIndicator(close, window=self.rsi_period).rsi()

        # Calculate MACD
        macd_indicator = MACD(close, window_fast=self.macd_fast, window_slow=self.macd_slow, window_sign=self.macd_signal)
        macd = macd_indicator.macd()
        macdsignal = macd_indicator.macd_signal()

        # Strategy logic
        if rsi.iloc[-1] < 30 and macd.iloc[-1] > macdsignal.iloc[-1]:
            return "buy"
        elif rsi.iloc[-1] > 70 and macd.iloc[-1] < macdsignal.iloc[-1]:
            return "sell"
        else:
            return "hold"

    def status(self):
        return {"bot": "RSIMACD", "status": "ready"}

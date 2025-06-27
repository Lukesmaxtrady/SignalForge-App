import pandas as pd

class TrendFollowBot:
    def __init__(self, ma_period=50):
        self.ma_period = ma_period

    def predict(self, data: pd.DataFrame):
        close = data['close']
        ma = close.rolling(window=self.ma_period).mean()
        if close.iloc[-1] > ma.iloc[-1]:
            return "buy"
        elif close.iloc[-1] < ma.iloc[-1]:
            return "sell"
        else:
            return "hold"

    def status(self):
        return {"bot": "TrendFollow", "status": "ready"}

import pandas as pd

class MeanReversionBot:
    def __init__(self, window=20, threshold=2.0):
        self.window = window
        self.threshold = threshold

    def predict(self, data: pd.DataFrame):
        close = data['close']
        mean = close.rolling(window=self.window).mean()
        std = close.rolling(window=self.window).std()
        if close.iloc[-1] < (mean.iloc[-1] - self.threshold * std.iloc[-1]):
            return "buy"
        elif close.iloc[-1] > (mean.iloc[-1] + self.threshold * std.iloc[-1]):
            return "sell"
        else:
            return "hold"

    def status(self):
        return {"bot": "MeanReversion", "status": "ready"}

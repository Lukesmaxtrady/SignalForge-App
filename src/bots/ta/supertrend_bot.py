import pandas as pd

class SupertrendBot:
    def __init__(self, period=10, multiplier=3):
        self.period = period
        self.multiplier = multiplier

    def _supertrend(self, data):
        # Simple Supertrend implementation (can be replaced with ta-lib or custom logic)
        high = data['high']
        low = data['low']
        close = data['close']
        atr = (high - low).rolling(window=self.period).mean()
        hl2 = (high + low) / 2
        final_upperband = hl2 + (self.multiplier * atr)
        final_lowerband = hl2 - (self.multiplier * atr)
        in_uptrend = True
        direction = []
        for i in range(len(close)):
            if i == 0:
                direction.append(in_uptrend)
                continue
            if close.iloc[i] > final_upperband.iloc[i-1]:
                in_uptrend = True
            elif close.iloc[i] < final_lowerband.iloc[i-1]:
                in_uptrend = False
            direction.append(in_uptrend)
        return direction

    def predict(self, data: pd.DataFrame):
        direction = self._supertrend(data)
        if direction[-1]:
            return "buy"
        else:
            return "sell"

    def status(self):
        return {"bot": "Supertrend", "status": "ready"}

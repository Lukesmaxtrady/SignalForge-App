import pandas as pd

class VolumeSpikeBot:
    def __init__(self, spike_ratio=2.0, window=20):
        self.spike_ratio = spike_ratio
        self.window = window

    def predict(self, data: pd.DataFrame):
        vol = data['volume']
        avg_vol = vol.rolling(window=self.window).mean()
        if vol.iloc[-1] > self.spike_ratio * avg_vol.iloc[-1]:
            return "buy"
        else:
            return "hold"

    def status(self):
        return {"bot": "VolumeSpike", "status": "ready"}

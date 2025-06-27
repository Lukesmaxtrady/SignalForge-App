import pandas as pd
import ta
from finta import TA as fta
import pandas_ta as pta

def add_ta_features(df):
    # Core TA indicators
    df["rsi"] = ta.momentum.RSIIndicator(df["close"]).rsi()
    bb = ta.volatility.BollingerBands(df["close"])
    df["bb_h"] = bb.bollinger_hband()
    df["bb_l"] = bb.bollinger_lband()
    df["sma_fast"] = ta.trend.sma_indicator(df["close"], window=10)
    df["sma_slow"] = ta.trend.sma_indicator(df["close"], window=50)
    df["ema21"] = fta.EMA(df, 21)
    macd = pta.macd(df["close"])
    df["macd"] = macd["MACD_12_26_9"]
    df["macdsig"] = macd["MACDs_12_26_9"]
    df["macdhist"] = macd["MACDh_12_26_9"]
    df["obv"] = ta.volume.OnBalanceVolumeIndicator(df["close"], df["volume"]).on_balance_volume()
    # Signals: trend, mean-reversion
    df["trend_signal"] = (df["sma_fast"] > df["sma_slow"]).astype(int) - (df["sma_fast"] < df["sma_slow"]).astype(int)
    df["meanrev_signal"] = (df["rsi"] < 30).astype(int) - (df["rsi"] > 70).astype(int)
    return df
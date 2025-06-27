import pandas as pd

def hybrid_signal(df, model=None):
    """
    Combines TA signals and ML meta-labels for fusion logic.
    - If ML model available, uses it as primary; else uses TA fallback.
    """
    if model:
        ml_preds = model.predict(df.drop(columns=["timestamp", "close"], errors='ignore').fillna(0))
        ta_trend = df["trend_signal"].values if "trend_signal" in df else [0]*len(df)
        final_signal = [m if m==t else 0 for m, t in zip(ml_preds, ta_trend)]
        df["hybrid_signal"] = final_signal
    else:
        df["hybrid_signal"] = df.get("trend_signal", 0)
    return df
import numpy as np

def fusion_signal(df, ml_model=None, stack_models=None, regime_col=None):
    """
    Advanced ensemble stacking (ML+TA+RL+custom logic).
    - stack_models: List of (model, weight) tuples.
    - regime_col: Optional regime label/column (e.g., bull/bear/volatile).
    """
    base_pred = df["trend_signal"] if "trend_signal" in df else np.zeros(len(df))
    ml_pred = ml_model.predict(df.drop(columns=["timestamp", "close"], errors='ignore').fillna(0)) if ml_model else np.zeros(len(df))
    stack_preds = [w * m.predict(df.drop(columns=["timestamp", "close"], errors='ignore').fillna(0)) for m, w in (stack_models or [])]
    stack_total = np.sum(stack_preds, axis=0) if stack_preds else 0

    # Regime switch (example: overlay in bullish regime only)
    if regime_col and regime_col in df:
        is_bull = df[regime_col] == "bull"
        signal = np.where(is_bull, ml_pred, base_pred)
    else:
        # Simple weighted fusion
        signal = 0.4 * base_pred + 0.4 * ml_pred + 0.2 * stack_total
        signal = np.round(signal)
    df["fusion_signal"] = signal
    return df
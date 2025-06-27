from src.signals.fusion_engine import fusion_signal
import pandas as pd

def run_batch_fusion_and_save(symbol, ml_model, stack_models=None, regime_col=None):
    df = pd.read_csv(f"data/ohlcv/{symbol}.csv")
    df = fusion_signal(df, ml_model=ml_model, stack_models=stack_models, regime_col=regime_col)
    df.to_csv(f"data/signals/{symbol}_signals.csv", index=False)
    print(f"Fusion batch for {symbol} saved to data/signals/{symbol}_signals.csv")
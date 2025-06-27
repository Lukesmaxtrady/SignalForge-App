from src.utils.scheduler import start_scheduler
from src.execution.batch_fusion import run_batch_fusion_and_save

def main():
    # Start background jobs
    start_scheduler()
    # Example: run batch for BTCUSDT (expand to all symbols/models as needed)
    # from src.signals.ml_engine import train_meta_model, predict_meta
    # df = ... # load features, target, etc.
    # model = train_meta_model(df, target_col="target")
    # run_batch_fusion_and_save("BTCUSDT", ml_model=model)
    print("Job runner and background scheduler started.")

if __name__ == "__main__":
    main()
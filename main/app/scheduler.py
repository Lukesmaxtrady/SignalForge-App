from apscheduler.schedulers.background import BackgroundScheduler
from .signal_pipeline import SignalPipeline
from .db import get_signals_collection

class SignalScheduler:
    def __init__(self, interval=60):
        self.pipeline = SignalPipeline()
        self.interval = interval
        self.scheduler = BackgroundScheduler()
        self.scheduler.add_job(self.run_job, 'interval', seconds=self.interval)

    def run_job(self):
        # Add your trading universe here
        for symbol in ["BTCUSDT", "ETHUSDT"]:
            signal = self.pipeline.generate_signal(symbol)
            get_signals_collection().insert_one(signal)

    def start(self):
        self.scheduler.start()

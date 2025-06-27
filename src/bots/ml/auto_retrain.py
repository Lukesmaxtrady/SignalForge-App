import logging
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger
from time import sleep
import threading

logger = logging.getLogger("bots.auto_retrain")

class AutoRetrainJob:
    def __init__(self, retrain_fn, interval_minutes=60):
        self.retrain_fn = retrain_fn
        self.interval = interval_minutes
        self.scheduler = BackgroundScheduler()
        self._running = False
        self._lock = threading.Lock()

    def start(self):
        with self._lock:
            if not self._running:
                self.scheduler.add_job(
                    self.safe_retrain,
                    trigger=IntervalTrigger(minutes=self.interval),
                    id='auto_retrain',
                    replace_existing=True
                )
                self.scheduler.start()
                self._running = True
                logger.info(f"AutoRetrainJob started, interval={self.interval} min")

    def stop(self):
        with self._lock:
            if self._running:
                self.scheduler.shutdown(wait=False)
                self._running = False
                logger.info("AutoRetrainJob stopped")

    def safe_retrain(self):
        try:
            logger.info("Running scheduled retrain job...")
            self.retrain_fn()
        except Exception as e:
            logger.error(f"Retrain job failed: {e}")

    def status(self):
        return {
            "job": "AutoRetrain",
            "status": "running" if self._running else "stopped",
            "interval": self.interval
        }

# Usage example:
# def retrain():
#     # Your retrain logic here
#     pass
#
# job = AutoRetrainJob(retrain, interval_minutes=60)
# job.start()

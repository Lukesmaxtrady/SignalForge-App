import schedule
import threading
import time
import logging
from src.utils.backup import nightly_backup

def start_scheduler(config=None):
    """
    Start the background scheduler.
    Accepts a config parameter (can be None).
    Runs as a daemon thread.
    """
    logging.info("Initializing background scheduler...")

    # Schedule the nightly backup
    schedule.every().day.at("03:00").do(nightly_backup)

    # You can add more scheduled jobs here, e.g.:
    # schedule.every(10).minutes.do(your_periodic_job)
    # if config and config.get("enable_analytics_job"):
    #     schedule.every().hour.do(run_analytics_job)

    def run_schedule():
        logging.info("Scheduler thread started.")
        while True:
            try:
                schedule.run_pending()
            except Exception as e:
                logging.error(f"Scheduler encountered error: {e}")
            time.sleep(1)

    # Only start the thread if we're not already running
    scheduler_thread = threading.Thread(target=run_schedule, daemon=True)
    scheduler_thread.start()
    logging.info("Scheduler running in background.")

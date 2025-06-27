import logging
from apscheduler.schedulers.background import BackgroundScheduler
from .manager import BotManager

logger = logging.getLogger("auto_retrain")
logging.basicConfig(level=logging.INFO)

def retrain_ml_bots(manager: BotManager):
    logger.info("Starting scheduled ML bot retraining...")
    manager.load_bots()
    for name, bot in manager.bots.items():
        if hasattr(bot, "retrain"):
            try:
                logger.info(f"Retraining bot: {name}")
                bot.retrain()
            except Exception as e:
                logger.error(f"Retraining failed for {name}: {e}")

def start_retrain_scheduler():
    manager = BotManager()
    scheduler = BackgroundScheduler(timezone="UTC")
    # Retrain every day at 3am UTC (change as needed)
    scheduler.add_job(lambda: retrain_ml_bots(manager), 'cron', hour=3)
    scheduler.start()
    logger.info("Retrain scheduler started. ML bots will retrain daily at 3am UTC.")

if __name__ == "__main__":
    start_retrain_scheduler()
    # Keep the script alive for scheduler
    import time
    try:
        while True:
            time.sleep(60)
    except (KeyboardInterrupt, SystemExit):
        logger.info("Retrain scheduler stopped.")

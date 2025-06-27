from .job_manager import add_job
from src.bots.ml.auto_retrain import retrain_all_models

def schedule_daily_retrain():
    add_job(retrain_all_models, trigger='interval', hours=24)

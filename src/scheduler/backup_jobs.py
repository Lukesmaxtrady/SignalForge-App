from .job_manager import add_job
from src.db.backup_restore import backup_database

def schedule_daily_backup():
    add_job(backup_database, trigger='cron', hour=3)  # 3am backup

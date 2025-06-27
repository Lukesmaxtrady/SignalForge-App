from .job_manager import add_job
from src.bots.utils.budget import check_budget

def schedule_budget_checks():
    add_job(check_budget, trigger='interval', hours=1)

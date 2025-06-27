from .job_manager import add_job

def event_window_task():
    # Add logic for event-specific scheduling (e.g., FOMC, CPI release)
    pass

def schedule_event_windows():
    add_job(event_window_task, trigger='cron', minute=0)

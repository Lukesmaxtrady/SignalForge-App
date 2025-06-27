from datetime import datetime, timedelta

class ScheduleManager:
    def __init__(self):
        self.jobs = []

    def add_job(self, func, trigger_time):
        self.jobs.append((func, trigger_time))

    def run_due_jobs(self):
        now = datetime.now()
        for func, trigger_time in list(self.jobs):
            if trigger_time <= now:
                func()
                self.jobs.remove((func, trigger_time))

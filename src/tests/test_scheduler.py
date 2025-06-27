import unittest
from src.scheduler.job_manager import JobManager

class TestScheduler(unittest.TestCase):
    def setUp(self):
        self.jobs = JobManager()
    def test_job_add(self):
        def foo(): pass
        self.jobs.add_job(foo, "test")
        self.assertEqual(len(self.jobs.jobs), 1)

import unittest
from src.bots.utils.budget import Budget

class TestPaidFeatures(unittest.TestCase):
    def test_budget_allocation(self):
        budget = Budget(100)
        self.assertTrue(budget.allocate(50))
        self.assertFalse(budget.allocate(60))

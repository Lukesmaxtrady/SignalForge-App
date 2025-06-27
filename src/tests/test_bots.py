import unittest
from src.bots.manager import BotManager

class TestBots(unittest.TestCase):
    def setUp(self):
        self.manager = BotManager()
    def test_bots_start(self):
        self.assertTrue(self.manager.launch_all())

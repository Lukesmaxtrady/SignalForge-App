import unittest
from src.db.db_manager import DBManager

class TestDB(unittest.TestCase):
    def setUp(self):
        self.db = DBManager()
    def test_connection(self):
        self.assertTrue(self.db.connect())

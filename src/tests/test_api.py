import unittest
from fastapi.testclient import TestClient
from src.main import app

class TestAPI(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)
    def test_health(self):
        resp = self.client.get("/health")
        self.assertEqual(resp.status_code, 200)

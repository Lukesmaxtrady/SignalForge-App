import unittest
from src.bots.security.scam_alert import ScamAlert

class TestSecurity(unittest.TestCase):
    def test_scam_alert(self):
        alert = ScamAlert()
        self.assertTrue(alert.check_for_scams("Beware of scam!"))

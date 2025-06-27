import logging

class ScamAlertSystem:
    def __init__(self):
        self.scam_keywords = ["scam", "rug pull", "phishing", "fraud", "exploit"]
        self.active_alerts = []

    def scan_message(self, message):
        detected = [kw for kw in self.scam_keywords if kw in message.lower()]
        if detected:
            alert = {
                "type": "SCAM_ALERT",
                "keywords": detected,
                "message": message
            }
            self.active_alerts.append(alert)
            logging.warning(f"Scam Alert: {alert}")
            return alert
        return None

    def list_alerts(self):
        return self.active_alerts

    def status(self):
        return {"feature": "scam_alert", "active": bool(self.active_alerts)}

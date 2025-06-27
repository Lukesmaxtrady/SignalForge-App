import logging

class HackDetectionSystem:
    def __init__(self):
        self.last_check = None
        self.alerts = []

    def scan_activity(self, event):
        suspicious_patterns = ["unauthorized access", "withdrawal anomaly", "API misuse"]
        found = [pattern for pattern in suspicious_patterns if pattern in event.lower()]
        if found:
            alert = {
                "type": "HACK_DETECTED",
                "patterns": found,
                "event": event
            }
            self.alerts.append(alert)
            logging.critical(f"Hack Alert: {alert}")
            return alert
        return None

    def list_alerts(self):
        return self.alerts

    def status(self):
        return {"feature": "hack_detection", "alerts": len(self.alerts)}

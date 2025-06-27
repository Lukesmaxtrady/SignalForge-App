import logging

class RiskAudit:
    def __init__(self):
        self.reports = []

    def run_audit(self, system_state):
        # Dummy checks; in real app, check balances, bot exposures, API activity, etc.
        issues = []
        if system_state.get("excess_leverage", False):
            issues.append("Excess leverage detected.")
        if not system_state.get("stoploss_enabled", True):
            issues.append("Stoploss is not enabled.")
        if system_state.get("api_exposure", 0) > 10:
            issues.append("Too many API keys active.")

        report = {
            "issues": issues,
            "timestamp": system_state.get("timestamp")
        }
        self.reports.append(report)
        logging.info(f"Risk audit: {report}")
        return report

    def get_reports(self):
        return self.reports

    def status(self):
        return {"feature": "risk_audit", "reports": len(self.reports)}

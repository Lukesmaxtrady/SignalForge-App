class ComplianceChecker:
    def __init__(self, jurisdiction="US"):
        self.jurisdiction = jurisdiction
        self.issues = []

    def check(self, action, params=None):
        # Very basic compliance logic, placeholder for full implementation
        if self.jurisdiction == "US" and action == "trade" and params:
            if params.get("leverage", 1) > 2:
                self.issues.append("Leverage over 2x not allowed in US.")
                return False
        return True

    def get_issues(self):
        return self.issues

    def status(self):
        return {"feature": "compliance", "jurisdiction": self.jurisdiction}

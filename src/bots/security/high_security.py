class HighSecurityMode:
    def __init__(self):
        self.enabled = False

    def enable(self):
        self.enabled = True

    def disable(self):
        self.enabled = False

    def status(self):
        return {"mode": "high_security", "enabled": self.enabled}

    def enforce(self, config):
        # Example: block risky bots, enforce 2FA, block new API keys
        config["max_leverage"] = 1
        config["require_2fa"] = True
        config["block_untested_bots"] = True
        return config

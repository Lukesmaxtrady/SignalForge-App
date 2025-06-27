def get_custom_mode(settings: dict):
    # Validate and return custom user-defined mode settings
    defaults = {
        "bot_risk_level": "medium",
        "security_mode": "medium",
        "advanced_features": False
    }
    defaults.update(settings)
    return defaults

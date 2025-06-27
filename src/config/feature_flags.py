import os

def is_feature_enabled(feature_name: str) -> bool:
    return os.getenv(f"FEATURE_{feature_name.upper()}", "false").lower() == "true"

def get_enabled_features():
    return [key[8:] for key, value in os.environ.items() if key.startswith("FEATURE_") and value.lower() == "true"]

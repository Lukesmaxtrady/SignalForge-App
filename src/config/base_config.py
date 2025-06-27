import os
import yaml

CONFIG_FILE = os.getenv("SIGNALFORGE_CONFIG", "signalforge_config.yaml")

def load_config():
    with open(CONFIG_FILE, "r") as f:
        return yaml.safe_load(f)

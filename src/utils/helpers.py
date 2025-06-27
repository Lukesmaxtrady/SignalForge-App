import yaml
import json

def load_yaml(path):
    with open(path, "r") as f:
        return yaml.safe_load(f)

def save_yaml(obj, path):
    with open(path, "w") as f:
        yaml.safe_dump(obj, f)

def load_json(path):
    with open(path, "r") as f:
        return json.load(f)

def save_json(obj, path):
    with open(path, "w") as f:
        json.dump(obj, f, indent=2)
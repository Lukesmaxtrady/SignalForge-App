import pandas as pd

def load_csv(path):
    try:
        return pd.read_csv(path)
    except Exception as e:
        from .logger import logger
        logger.error(f"Failed to load CSV: {path} - {str(e)}")
        return None

def load_json(path):
    import json
    try:
        with open(path, 'r') as f:
            return json.load(f)
    except Exception as e:
        from .logger import logger
        logger.error(f"Failed to load JSON: {path} - {str(e)}")
        return None

import requests

def get_json(url, headers=None, params=None):
    try:
        response = requests.get(url, headers=headers, params=params, timeout=10)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        from .logger import logger
        logger.error(f"API GET failed: {url} - {str(e)}")
        return None

def post_json(url, data=None, headers=None):
    try:
        response = requests.post(url, json=data, headers=headers, timeout=10)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        from .logger import logger
        logger.error(f"API POST failed: {url} - {str(e)}")
        return None

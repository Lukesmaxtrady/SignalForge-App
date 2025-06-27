import os
from dotenv import load_dotenv

def load_env(env_path: str = ".env"):
    load_dotenv(env_path)
    return {k: v for k, v in os.environ.items()}

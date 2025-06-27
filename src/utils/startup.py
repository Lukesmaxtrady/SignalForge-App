import os
import sys
import logging

def startup_check(required_keys):
    missing = [k for k in required_keys if not os.getenv(k)]
    if missing:
        logging.error(f"Missing environment variables: {', '.join(missing)}")
        sys.exit(1)

import logging
import os
from logging.handlers import RotatingFileHandler

def get_logger(
    name: str = "omegasignalpro",
    level: int = logging.INFO,
    log_to_console: bool = False
) -> logging.Logger:
    """
    Returns a configured logger with rotating file handler.
    Optionally logs to console as well.

    Args:
        name (str): Logger name.
        level (int): Logging level.
        log_to_console (bool): If True, also logs to console.

    Returns:
        logging.Logger
    """
    os.makedirs("logs", exist_ok=True)
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Prevent duplicate handlers
    log_file = os.path.abspath("logs/app.log")
    handler_exists = any(
        isinstance(h, RotatingFileHandler) and getattr(h, 'baseFilename', None) == log_file
        for h in logger.handlers
    )
    if not handler_exists:
        file_handler = RotatingFileHandler(log_file, maxBytes=5_000_000, backupCount=7)
        formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    # Optionally add console output
    if log_to_console and not any(isinstance(h, logging.StreamHandler) for h in logger.handlers):
        stream_handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s')
        stream_handler.setFormatter(formatter)
        logger.addHandler(stream_handler)

    return logger

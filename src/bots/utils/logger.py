import logging

def setup_logger(name="signalforge", log_file="logs/app.log", level=logging.INFO):
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(name)s: %(message)s')
    handler = logging.FileHandler(log_file)
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    if not logger.handlers:
        logger.addHandler(handler)
    return logger

logger = setup_logger()

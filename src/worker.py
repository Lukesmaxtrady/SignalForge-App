import asyncio
import logging
import yaml
import os
from src.execution.executor import TradingEngine
from src.utils.scheduler import start_scheduler
from src.utils.startup import startup_check

if __name__ == "__main__":
    startup_check(["MONGODB_URI", "BITGET_API_KEY", "BITGET_API_SECRET"])

    logging.basicConfig(level=logging.INFO)
    logging.info("Starting SignalForge Worker...")

    with open("config/config.yaml") as f:
        config = yaml.safe_load(f)

    start_scheduler(config)

    engine = TradingEngine(config)
    asyncio.run(engine.run_async())

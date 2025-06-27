from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from src.api import (
    user_routes, bot_routes, analytics_routes, 
    signals_routes, security_routes, webhook_routes
)
import logging
import os
import yaml
import sys
import threading

from src.utils.scheduler import start_scheduler
from src.execution.executor import TradingEngine

CONFIG_PATH = "config/config.yaml"

def setup_logging():
    os.makedirs("logs", exist_ok=True)
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[
            logging.FileHandler("logs/omega_main.log"),
            logging.StreamHandler(sys.stdout),
        ]
    )

def load_config():
    if not os.path.isfile(CONFIG_PATH):
        logging.error(f"Config file not found: {CONFIG_PATH}")
        sys.exit(1)
    with open(CONFIG_PATH, "r") as f:
        config = yaml.safe_load(f)
    return config

def ensure_dirs():
    needed = [
        "data/ohlcv", "data/alpha", "data/signals", "data/trades",
        "data/reports", "data/backups", "src/models", "logs"
    ]
    for d in needed:
        os.makedirs(d, exist_ok=True)

app = FastAPI(title="SignalForge API", version="1.0.0")

# Permissive CORS for development, restrict in production environment as needed
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Restrict this in production to your frontend domains
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register API routers
app.include_router(user_routes.router)
app.include_router(bot_routes.router)
app.include_router(analytics_routes.router)
app.include_router(signals_routes.router)
app.include_router(security_routes.router)
app.include_router(webhook_routes.router)

@app.on_event("startup")
async def on_startup():
    setup_logging()
    logging.info("Starting OmegaSignalPro FastAPI server...")
    ensure_dirs()

    try:
        config = load_config()
        logging.info(f"Loaded config: {config.get('app_name', 'OmegaSignalPro')}")
    except Exception as e:
        logging.error(f"Failed to load config: {e}")
        sys.exit(1)

    # Start the scheduler in a background daemon thread
    try:
        scheduler_thread = threading.Thread(target=start_scheduler, args=(config,), daemon=True)
        scheduler_thread.start()
        logging.info("Scheduler started.")
    except Exception as e:
        logging.error(f"Scheduler error: {e}")

    # Initialize and start the trading engine's run_async in a daemon thread
    try:
        engine = TradingEngine(config)
        app.state.trading_engine = engine  # Save for later use/access in routes if needed
        engine_thread = threading.Thread(target=engine.run_async, daemon=True)
        engine_thread.start()
        logging.info("Trading engine launched.")
    except Exception as e:
        logging.error(f"Trading engine failed: {e}")

@app.get("/")
def root():
    return {"status": "ok", "app": "SignalForge API", "version": "1.0.0"}

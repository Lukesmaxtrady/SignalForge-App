import logging
from typing import List, Dict, Any
from src.bots.registry import BOT_REGISTRY
from src.bots.performance import BotPerformanceTracker
from src.bots.risk_control import BotRiskController

logger = logging.getLogger("bots.manager")

class BotManager:
    """
    BotManager loads, runs, manages, and monitors all registered bots,
    with performance tracking and risk control support.
    """
    def __init__(self):
        self.bots = {}  # Dict[str, object]
        self.tracker = BotPerformanceTracker()
        self.risk_control = BotRiskController()
        self.load_bots()

    def load_bots(self) -> None:
        """Instantiate all registered bots and store them in self.bots."""
        self.bots = {}
        for name, bot_cls in BOT_REGISTRY.items():
            try:
                bot = bot_cls()
                self.bots[name] = bot
                logger.info(f"Loaded bot: {name}")
            except Exception as e:
                logger.error(f"Failed to load bot {name}: {e}")

    def start_bot(self, bot_name: str) -> bool:
        bot = self.bots.get(bot_name)
        if bot and self.risk_control.allow_run(bot):
            try:
                bot.start()
                logger.info(f"Started bot: {bot_name}")
                return True
            except Exception as e:
                logger.error(f"Failed to start bot {bot_name}: {e}")
        return False

    def stop_bot(self, bot_name: str) -> bool:
        bot = self.bots.get(bot_name)
        if bot:
            try:
                bot.stop()
                logger.info(f"Stopped bot: {bot_name}")
                return True
            except Exception as e:
                logger.error(f"Failed to stop bot {bot_name}: {e}")
        return False

    def get_bot_status(self, bot_name: str) -> Any:
        bot = self.bots.get(bot_name)
        if bot:
            try:
                return bot.status()
            except Exception as e:
                logger.error(f"Error getting status for bot {bot_name}: {e}")
                return "error"
        return None

    def list_bots(self) -> List[str]:
        """List all available bot names."""
        return list(self.bots.keys())

    def start_all(self) -> None:
        """Start all bots that pass risk control."""
        for name in self.bots:
            self.start_bot(name)

    def stop_all(self) -> None:
        """Stop all bots."""
        for name in self.bots:
            self.stop_bot(name)

    def get_status(self) -> List[Dict[str, Any]]:
        """Get status of all bots."""
        statuses = []
        for name, bot in self.bots.items():
            try:
                status = bot.status()
            except Exception as e:
                logger.error(f"Error getting status for bot {name}: {e}")
                status = "error"
            statuses.append({"bot": name, "status": status})
        return statuses

    def run_all_once(self) -> None:
        """For bots with a single-run method (not continuous), run once and log result."""
        for name, bot in self.bots.items():
            try:
                if hasattr(bot, "run") and self.risk_control.allow_run(bot):
                    result = bot.run()
                    self.tracker.log_performance(bot, result)
                    logger.info(f"Ran bot: {name}, result: {result}")
            except Exception as e:
                logger.error(f"Error running bot {name}: {e}")

# ---- API Helper functions for src/api/bot_routes.py ----

_manager = BotManager()

def launch_bot(bot_name: str) -> bool:
    return _manager.start_bot(bot_name)

def stop_bot(bot_name: str) -> bool:
    return _manager.stop_bot(bot_name)

def get_bot_status(bot_name: str) -> Any:
    return _manager.get_bot_status(bot_name)

def list_bots() -> List[str]:
    return _manager.list_bots()

def start_all_bots():
    _manager.start_all()

def stop_all_bots():
    _manager.stop_all()

def get_all_status():
    return _manager.get_status()

def run_all_bots_once():
    _manager.run_all_once()

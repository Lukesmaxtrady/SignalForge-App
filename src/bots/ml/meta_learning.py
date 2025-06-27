from __future__ import annotations
from typing import List, Any, Dict, Optional
import threading
import logging

logger = logging.getLogger("bots.meta_learning")

class MetaLearningBot:
    def __init__(self, models: Optional[List[Any]] = None) -> None:
        self._models_lock = threading.Lock()
        self.models: List[Any] = models or []
        self._running = False

    def add_bot(self, bot: Any):
        with self._models_lock:
            self.models.append(bot)
            logger.info(f"Added bot to MetaLearningBot: {getattr(bot, 'name', str(bot))}")

    def remove_bot(self, bot: Any):
        with self._models_lock:
            self.models = [m for m in self.models if m is not bot]
            logger.info(f"Removed bot from MetaLearningBot: {getattr(bot, 'name', str(bot))}")

    def clear_bots(self):
        with self._models_lock:
            self.models = []

    def _vote(self, signals: List[str]) -> str:
        buy  = signals.count("buy")
        sell = signals.count("sell")
        hold = signals.count("hold")
        if buy  > max(sell, hold):
            return "buy"
        if sell > max(buy, hold):
            return "sell"
        return "hold"

    def predict(self, features) -> Dict[str, Any]:
        signals = []
        errors = []
        with self._models_lock:
            bots = list(self.models)
        for bot in bots:
            try:
                if hasattr(bot, "predict"):
                    res = bot.predict(features)
                else:
                    res = bot.run(features)
                signal = res if isinstance(res, str) else res.get("signal", "hold")
                signals.append(signal)
            except Exception as e:
                logger.error(f"MetaLearningBot: Error in child bot {getattr(bot, 'name', str(bot))}: {e}")
                errors.append(str(e))
                signals.append("hold")
        final = self._vote(signals)
        return {"signal": final, "votes": signals, "errors": errors}

    def run(self, features):
        return self.predict(features)

    def start(self):
        with self._models_lock:
            for bot in self.models:
                if hasattr(bot, "start"):
                    try:
                        bot.start()
                        logger.info(f"Started child bot: {getattr(bot, 'name', str(bot))}")
                    except Exception as e:
                        logger.warning(f"Failed to start bot {getattr(bot, 'name', str(bot))}: {e}")
        self._running = True

    def stop(self):
        with self._models_lock:
            for bot in self.models:
                if hasattr(bot, "stop"):
                    try:
                        bot.stop()
                        logger.info(f"Stopped child bot: {getattr(bot, 'name', str(bot))}")
                    except Exception as e:
                        logger.warning(f"Failed to stop bot {getattr(bot, 'name', str(bot))}: {e}")
        self._running = False

    def status(self):
        with self._models_lock:
            bots_status = []
            for bot in self.models:
                if hasattr(bot, "status"):
                    try:
                        st = bot.status()
                    except Exception as e:
                        st = {"error": str(e)}
                else:
                    st = {"info": "no status()"}
                bots_status.append(st)
        return {
            "bot": "MetaLearning",
            "status": "running" if self._running else "stopped",
            "n_children": len(self.models),
            "children": bots_status,
        }

MetaLearning = MetaLearningBot

import threading
import logging
import time

logger = logging.getLogger("bots.risk_control")

class BotRiskController:
    def __init__(self, failure_limit=3, cooldown_secs=600):
        self._lock = threading.Lock()
        self._failures = {}    # bot_name -> count
        self._cooldowns = {}   # bot_name -> cooldown-until timestamp
        self.failure_limit = failure_limit
        self.cooldown_secs = cooldown_secs

    def allow_run(self, bot):
        name = getattr(bot, "name", bot.__class__.__name__)
        with self._lock:
            cooldown_until = self._cooldowns.get(name, 0)
            now = time.time()
            if now < cooldown_until:
                logger.warning(f"Bot {name} is in cooldown until {cooldown_until}.")
                return False
            failures = self._failures.get(name, 0)
            if failures >= self.failure_limit:
                logger.error(f"Bot {name} disabled due to failures ({failures} ≥ {self.failure_limit})")
                return False
            return True

    def report_failure(self, bot):
        name = getattr(bot, "name", bot.__class__.__name__)
        with self._lock:
            failures = self._failures.get(name, 0) + 1
            self._failures[name] = failures
            if failures >= self.failure_limit:
                self._cooldowns[name] = time.time() + self.cooldown_secs
                logger.error(f"Bot {name} entered cooldown for {self.cooldown_secs} seconds.")

    def release(self, bot):
        name = getattr(bot, "name", bot.__class__.__name__)
        with self._lock:
            self._failures.pop(name, None)
            self._cooldowns.pop(name, None)
            logger.info(f"Bot {name} released from risk control.")

    def get_status(self, bot):
        name = getattr(bot, "name", bot.__class__.__name__)
        with self._lock:
            return {
                "failures": self._failures.get(name, 0),
                "cooldown_until": self._cooldowns.get(name, 0),
            }

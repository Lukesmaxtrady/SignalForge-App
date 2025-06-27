import threading
import logging
from datetime import datetime

logger = logging.getLogger("bots.performance")


class BotPerformanceTracker:
    def __init__(self):
        self._lock = threading.Lock()
        self._stats = {}  # bot name -> stat dict

    def log_performance(self, bot, result):
        """Log the result of a bot run."""
        name = getattr(bot, "name", bot.__class__.__name__)
        with self._lock:
            stats = self._stats.setdefault(name, {
                "run_count": 0,
                "success": 0,
                "failures": 0,
                "last_result": None,
                "last_run": None,
                "last_error": None,
            })
            stats["run_count"] += 1
            stats["last_run"] = datetime.utcnow().isoformat()
            stats["last_result"] = result
            # Optionally, inspect the result for error
            if isinstance(result, dict) and ("error" in result and result["error"]):
                stats["failures"] += 1
                stats["last_error"] = result.get("error")
            else:
                stats["success"] += 1
                stats["last_error"] = None
        logger.info(f"Performance updated for {name}: {stats}")

    def get_stats(self, name):
        """Get stats for a single bot."""
        with self._lock:
            return dict(self._stats.get(name, {}))  # return a copy

    def get_all_stats(self):
        """Get stats for all bots."""
        with self._lock:
            return {k: dict(v) for k, v in self._stats.items()}

    def reset_stats(self, name=None):
        """Reset stats for one or all bots."""
        with self._lock:
            if name:
                self._stats.pop(name, None)
            else:
                self._stats.clear()

    def summary(self):
        """Return a summary of all bot performances."""
        with self._lock:
            return {
                name: {
                    "run_count": s["run_count"],
                    "success": s["success"],
                    "failures": s["failures"],
                    "last_run": s["last_run"],
                }
                for name, s in self._stats.items()
            }


# Singleton tracker (import this elsewhere)
tracker = BotPerformanceTracker()

def get_performance_summary():
    """For API: Return a summary of all bot performances."""
    return tracker.summary()

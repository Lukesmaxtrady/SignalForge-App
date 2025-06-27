# src/bots/bot_base.py
import threading

class BotBase:
    def start(self):
        if hasattr(self, '_running') and self._running:
            return
        self._running = True
        self._thread = threading.Thread(target=self.run)
        self._thread.start()
    def stop(self):
        self._running = False
    def status(self):
        return {"bot": self.__class__.__name__, "status": "ready"}
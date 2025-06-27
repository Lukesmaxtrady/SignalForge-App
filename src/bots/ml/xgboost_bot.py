import numpy as np
import threading
import logging
import xgboost as xgb
import joblib
import os

logger = logging.getLogger("bots.xgboost")

class XGBoostBot:
    def __init__(self, model_path=None):
        self.model_path = model_path or os.getenv("XGBOOST_MODEL_PATH", "model/xgboost_bot.model")
        self._model_lock = threading.Lock()
        self._model = None
        self._running = False
        self._ensure_model_loaded()

    def _ensure_model_loaded(self):
        with self._model_lock:
            if self._model is None:
                if self.model_path.endswith(".model"):
                    self._model = xgb.Booster()
                    self._model.load_model(self.model_path)
                else:
                    self._model = joblib.load(self.model_path)

    def predict(self, features):
        if not isinstance(features, np.ndarray):
            features = np.array(features).reshape(1, -1)
        self._ensure_model_loaded()
        dm = xgb.DMatrix(features)
        proba = self._model.predict(dm)
        signal = "buy" if proba[-1] > 0.5 else "sell"
        return {
            "signal": signal,
            "confidence": float(proba[-1])
        }

    def run(self, features):
        return self.predict(features)

    def start(self):
        self._running = True
        logger.info("XGBoostBot started.")

    def stop(self):
        self._running = False
        logger.info("XGBoostBot stopped.")

    def status(self):
        return {
            "bot": "XGBoost",
            "status": "running" if self._running else "stopped",
            "model_loaded": self._model is not None
        }

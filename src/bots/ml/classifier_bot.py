import numpy as np
import threading
import logging
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

logger = logging.getLogger("bots.classifier")

class ClassifierBot:
    def __init__(self, model_path=None):
        self.model_path = model_path or os.getenv("CLASSIFIER_MODEL_PATH", "model/classifier_bot.pkl")
        self._model_lock = threading.Lock()
        self._model = None
        self._running = False
        self._ensure_model_loaded()

    def _ensure_model_loaded(self):
        with self._model_lock:
            if self._model is None:
                if not os.path.isfile(self.model_path):
                    raise FileNotFoundError(f"Classifier model file not found: {self.model_path}")
                self._model = joblib.load(self.model_path)

    def predict(self, features):
        if not isinstance(features, np.ndarray):
            features = np.array(features).reshape(1, -1)
        self._ensure_model_loaded()
        pred = self._model.predict(features)[0]
        proba = self._model.predict_proba(features)[0]
        return {
            "signal": pred,
            "confidence": float(np.max(proba)),
            "proba": proba.tolist()
        }

    def run(self, features):
        return self.predict(features)

    def start(self):
        self._running = True
        logger.info("ClassifierBot started.")

    def stop(self):
        self._running = False
        logger.info("ClassifierBot stopped.")

    def status(self):
        return {
            "bot": "Classifier",
            "status": "running" if self._running else "stopped",
            "model_loaded": self._model is not None
        }

import numpy as np
import threading
import logging
import os

try:
    import tensorflow as tf
    TENSORFLOW_AVAILABLE = True
except ImportError:
    tf = None
    TENSORFLOW_AVAILABLE = False

logger = logging.getLogger("bots.lstm")

class LSTMPredictor:
    def __init__(self, model_path=None):
        self.model_path = model_path or os.getenv("LSTM_MODEL_PATH", "model/lstm_predictor.h5")
        self._model_lock = threading.Lock()
        self._model = None
        self._running = False
        if not TENSORFLOW_AVAILABLE:
            raise ImportError("TensorFlow is not installed. LSTMPredictor cannot be used.")
        self._ensure_model_loaded()

    def _ensure_model_loaded(self):
        with self._model_lock:
            if self._model is None:
                if not os.path.isfile(self.model_path):
                    raise FileNotFoundError(f"LSTM model file not found: {self.model_path}")
                self._model = tf.keras.models.load_model(self.model_path)

    def predict(self, sequence):
        if not isinstance(sequence, np.ndarray):
            raise TypeError("Input 'sequence' must be a np.ndarray.")
        if sequence.ndim != 3:
            raise ValueError(f"Input shape must be (batch, timesteps, features), got {sequence.shape}")
        self._ensure_model_loaded()
        pred = self._model.predict(sequence)
        if pred.ndim == 2:
            return {"future_price": float(pred[-1, 0]), "all": pred.flatten().tolist()}
        elif pred.ndim == 3:
            return {"future_price": float(pred[-1, -1, 0]), "all": pred.flatten().tolist()}
        else:
            raise RuntimeError(f"Unexpected model prediction shape: {pred.shape}")

    def run(self, sequence):
        return self.predict(sequence)

    def start(self):
        self._running = True
        logger.info("LSTMPredictor started.")

    def stop(self):
        self._running = False
        logger.info("LSTMPredictor stopped.")

    def status(self):
        return {
            "bot": "LSTM",
            "status": "running" if self._running else "stopped",
            "model_loaded": self._model is not None
        }

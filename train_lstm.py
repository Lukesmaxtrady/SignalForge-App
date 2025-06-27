# train_lstm.py

import numpy as np
import tensorflow as tf
import os

# For reproducibility
np.random.seed(42)
tf.random.set_seed(42)

# Make sure the model directory exists
os.makedirs("model", exist_ok=True)

# Dummy LSTM Model: for 10 timesteps, 5 features, predicts 1 value
model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(10, 5)),
    tf.keras.layers.LSTM(16),
    tf.keras.layers.Dense(1)
])

# Use full name for loss to avoid load issues
model.compile(optimizer="adam", loss="mean_squared_error")
model.summary()

# Dummy data (100 samples, 10 timesteps, 5 features)
X = np.random.randn(100, 10, 5)
y = np.random.randn(100, 1)
model.fit(X, y, epochs=2, verbose=1)

# Save the model as .h5 (legacy format, matches your codebase)
model.save("model/lstm_predictor.h5")
print("Dummy LSTM model saved to model/lstm_predictor.h5")

# Test that it loads without compilation (should not error)
try:
    tf.keras.models.load_model("model/lstm_predictor.h5", compile=False)
    print("Model file verified and can be loaded successfully.")
except Exception as e:
    print("ERROR: Model file could not be loaded!", e)

import numpy as np
import xgboost as xgb
import os

# Generate fake data
X = np.random.randn(1000, 10)
y = np.random.randint(0, 2, size=1000)

# Train a simple XGBoost classifier
model = xgb.XGBClassifier(n_estimators=10, use_label_encoder=False, eval_metric='logloss')
model.fit(X, y)

# Ensure model directory exists
os.makedirs("model", exist_ok=True)

# Save the model to model/xgboost_bot.model
model.save_model("model/xgboost_bot.model")

print("XGBoost model trained and saved to model/xgboost_bot.model")

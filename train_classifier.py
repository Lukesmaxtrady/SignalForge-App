import numpy as np
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

# Generate some fake data (10 features, 1000 samples, binary target)
X = np.random.randn(1000, 10)
y = np.random.randint(0, 2, size=1000)

# Train a simple classifier
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X, y)

# Ensure the directory exists
os.makedirs("model", exist_ok=True)

# Save the model to model/classifier_bot.pkl
joblib.dump(clf, "model/classifier_bot.pkl")

print("Model trained and saved to model/classifier_bot.pkl")

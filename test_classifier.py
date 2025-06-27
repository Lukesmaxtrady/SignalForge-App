import joblib
model = joblib.load("model/classifier_bot.pkl")
print(model.predict([[0]*10]))

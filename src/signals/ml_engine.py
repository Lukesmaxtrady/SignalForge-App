import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier
import xgboost as xgb
from catboost import CatBoostClassifier
import optuna
import os

def train_meta_model(df, target_col="target", model_type="xgboost", optimize=False, save_path=None):
    X = df.drop(columns=[target_col, "timestamp", "close"], errors='ignore').fillna(0)
    y = df[target_col]
    if model_type == "xgboost":
        model = xgb.XGBClassifier(n_estimators=100, max_depth=5, use_label_encoder=False, eval_metric="logloss")
    elif model_type == "catboost":
        model = CatBoostClassifier(verbose=0)
    else:
        model = RandomForestClassifier()
    if optimize:
        def objective(trial):
            params = {
                "n_estimators": trial.suggest_int("n_estimators", 50, 200),
                "max_depth": trial.suggest_int("max_depth", 2, 12)
            }
            model.set_params(**params)
            model.fit(X, y)
            return model.score(X, y)
        study = optuna.create_study(direction="maximize")
        study.optimize(objective, n_trials=10)
        model.set_params(**study.best_params)
    model.fit(X, y)
    if save_path:
        joblib.dump(model, save_path)
    return model

def predict_meta(model, df):
    X = df.drop(columns=["timestamp", "close"], errors='ignore').fillna(0)
    return model.predict(X)
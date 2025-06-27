import logging

logger = logging.getLogger("bots.registry")

# Try/except imports so the app starts even if some bots have issues.
def safe_import(bot_name, import_path):
    try:
        module_path, cls_name = import_path.rsplit(".", 1)
        mod = __import__(module_path, fromlist=[cls_name])
        return getattr(mod, cls_name)
    except Exception as e:
        logger.warning(f"Bot '{bot_name}' failed to import from {import_path}: {e}")
        return None

BOT_REGISTRY = {
    "RSI_MACD": safe_import("RSI_MACD", "src.bots.ta.rsi_macd_bot.RSIMACDBot"),
    "TREND_FOLLOW": safe_import("TREND_FOLLOW", "src.bots.ta.trend_follow_bot.TrendFollowBot"),
    "MEAN_REVERSION": safe_import("MEAN_REVERSION", "src.bots.ta.mean_reversion_bot.MeanReversionBot"),
    "VOLUME_SPIKE": safe_import("VOLUME_SPIKE", "src.bots.ta.volume_spike_bot.VolumeSpikeBot"),
    "SUPERTREND": safe_import("SUPERTREND", "src.bots.ta.supertrend_bot.SupertrendBot"),
    "CLASSIFIER": safe_import("CLASSIFIER", "src.bots.ml.classifier_bot.ClassifierBot"),
    "XGBOOST": safe_import("XGBOOST", "src.bots.ml.xgboost_bot.XGBoostBot"),
    "META_LEARNING": safe_import("META_LEARNING", "src.bots.ml.meta_learning.MetaLearningBot"),
    "LSTM": safe_import("LSTM", "src.bots.ml.lstm_predictor.LSTMPredictor"),
}

# Remove None entries if import failed
BOT_REGISTRY = {k: v for k, v in BOT_REGISTRY.items() if v is not None}

# Utility: List all available bots
def get_signals():
    return [{"id": k, "name": k, "class_name": v.__name__} for k, v in BOT_REGISTRY.items()]

# Utility: Get bot by registry key
def get_signal_by_id(signal_id):
    bot_cls = BOT_REGISTRY.get(signal_id)
    if bot_cls:
        return {"id": signal_id, "name": bot_cls.__name__}
    return None

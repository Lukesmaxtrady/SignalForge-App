from pymongo import MongoClient
from .config import MONGODB_URI

client = MongoClient(MONGODB_URI)
db = client.signalforge

def get_signals_collection():
    return db.signals

def get_pnl_collection():
    return db.pnl

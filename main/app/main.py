from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from .db import get_signals_collection, get_pnl_collection
from .schemas import Signal, PnLEntry, SignalRequest
from .signal_pipeline import SignalPipeline
from .telegram_bot import TelegramBot
from .scheduler import SignalScheduler

app = FastAPI()
origins = ["*"]  # Change for prod

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)

signal_pipeline = SignalPipeline()
telegram_bot = TelegramBot()
scheduler = SignalScheduler(interval=60)  # Every minute
scheduler.start()

@app.get("/health")
def health_check():
    try:
        get_signals_collection().find_one()
        return {"status": "ok"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/generate_signal", response_model=Signal)
def generate_signal(req: SignalRequest):
    signal = signal_pipeline.generate_signal(req.symbol)
    get_signals_collection().insert_one(signal)
    return signal

@app.get("/signals", response_model=list[Signal])
def list_signals(symbol: str = None):
    q = {}
    if symbol:
        q["symbol"] = symbol
    signals = list(get_signals_collection().find(q).sort("timestamp", -1).limit(50))
    for s in signals:
        s["id"] = str(s["_id"])
        s.pop("_id", None)
    return signals

@app.post("/send_signal")
def send_signal_to_telegram(signal_id: str, chat_id: str):
    signal = get_signals_collection().find_one({"_id": signal_id})
    if not signal:
        raise HTTPException(status_code=404, detail="Signal not found")
    msg = f"Signal: {signal['symbol']} {signal['signal_type']} (conf: {signal['confidence']:.2f})\n{signal['reason']}"
    sent = telegram_bot.send_message(chat_id, msg)
    if not sent:
        raise HTTPException(status_code=500, detail="Telegram send failed")
    return {"ok": True}

@app.get("/pnl", response_model=list[PnLEntry])
def get_pnl():
    entries = list(get_pnl_collection().find().sort("timestamp", -1).limit(100))
    for e in entries:
        e["id"] = str(e["_id"])
        e.pop("_id", None)
    return entries

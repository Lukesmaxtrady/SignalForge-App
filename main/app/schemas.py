from pydantic import BaseModel, Field
from typing import List, Optional

class Signal(BaseModel):
    symbol: str
    signal_type: str  # 'buy' or 'sell'
    confidence: float
    timestamp: int
    reason: str
    id: Optional[str] = None

class PnLEntry(BaseModel):
    signal_id: str
    pnl: float
    timestamp: int

class SignalRequest(BaseModel):
    symbol: str

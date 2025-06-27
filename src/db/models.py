from pydantic import BaseModel
from typing import List, Optional

class User(BaseModel):
    id: str
    username: str
    email: str
    created_at: Optional[str]

class BotPerformance(BaseModel):
    bot_name: str
    pnl: float
    win_rate: float
    sharpe_ratio: float
    trades: List[dict]
    timestamp: str

import numpy as np

class RiskManager:
    def __init__(self, max_daily_loss=0.05, max_drawdown=0.10, max_pos_size=0.2):
        self.max_daily_loss = max_daily_loss
        self.max_drawdown = max_drawdown
        self.max_pos_size = max_pos_size
        self.daily_loss = 0
        self.high_watermark = 0
        self.position_risk = {}

    def check_risk(self, pnl, equity, pos_size, symbol=None):
        risk_breaches = []
        if self.daily_loss + pnl < -self.max_daily_loss * equity:
            risk_breaches.append("daily_loss_limit")
        if (self.high_watermark - equity) > self.max_drawdown * self.high_watermark:
            risk_breaches.append("drawdown_limit")
        if pos_size > self.max_pos_size * equity:
            risk_breaches.append("position_size_limit")
        if symbol:
            pos_risk = self.position_risk.get(symbol, 0)
            if pos_risk > self.max_pos_size * equity:
                risk_breaches.append(f"{symbol}_position_size_limit")
        return risk_breaches

    def update_daily(self, pnl):
        self.daily_loss += pnl
        if self.high_watermark < pnl:
            self.high_watermark = pnl
class CapitalAllocator:
    def __init__(self, total_equity, allocations=None):
        self.total_equity = total_equity
        # Example: per-symbol allocation
        self.allocations = allocations or {}

    def allocate(self, symbol, risk_score=1.0):
        # Dynamic: scale by risk, vol, model confidence, etc.
        base_alloc = self.allocations.get(symbol, 1.0 / max(1, len(self.allocations) or 1))
        risk_adj = min(1.0, max(0.2, risk_score))
        capital = self.total_equity * base_alloc * risk_adj
        return capital
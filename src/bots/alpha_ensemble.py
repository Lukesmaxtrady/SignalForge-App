class AlphaEnsemble:
    """Fuses bot predictions (stacking, voting, regime-switching)."""
    def __init__(self, bots):
        self.bots = bots

    def predict(self, data):
        preds = [bot.predict(data) for bot in self.bots]
        # Majority vote for signal
        buy_votes = sum(1 for p in preds if p == "buy")
        sell_votes = sum(1 for p in preds if p == "sell")
        if buy_votes > sell_votes:
            return "buy"
        elif sell_votes > buy_votes:
            return "sell"
        else:
            return "hold"

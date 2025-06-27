class ROIAnalyzer:
    def __init__(self):
        self.trades = []

    def log_trade(self, entry_price, exit_price, size):
        self.trades.append({'entry': entry_price, 'exit': exit_price, 'size': size})

    def calculate_roi(self):
        roi = 0
        for t in self.trades:
            roi += ((t['exit'] - t['entry']) / t['entry']) * t['size']
        total_size = sum([t['size'] for t in self.trades]) or 1
        return roi / total_size

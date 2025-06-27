class ShadowBot:
    """Runs bot logic in 'shadow' (simulation) mode for safe testing."""

    def __init__(self, real_bot):
        self.real_bot = real_bot
        self.simulated_results = []

    def run(self, data):
        # Run without executing trades
        result = self.real_bot.simulate(data)
        self.simulated_results.append(result)
        return result

    def get_history(self):
        return self.simulated_results

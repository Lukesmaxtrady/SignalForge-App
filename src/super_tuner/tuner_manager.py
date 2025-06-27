class TunerManager:
    def __init__(self, bot_registry):
        self.bot_registry = bot_registry

    def set_weights(self, bot_name, weights: dict):
        if bot_name in self.bot_registry:
            self.bot_registry[bot_name].set_weights(weights)
            return True
        return False

    def get_current_weights(self, bot_name):
        return self.bot_registry.get(bot_name, {}).get_weights() if bot_name in self.bot_registry else {}

    def manual_override(self, bot_name, param, value):
        if bot_name in self.bot_registry:
            setattr(self.bot_registry[bot_name], param, value)
            return True
        return False

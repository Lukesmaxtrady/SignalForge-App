class EdgeMeter:
    def __init__(self):
        self.metrics = []

    def add_metric(self, name, value):
        self.metrics.append((name, value))

    def calculate_edge(self):
        # Simple average edge (customize as needed)
        if not self.metrics:
            return 0.0
        return sum([v for _, v in self.metrics]) / len(self.metrics)

class BudgetControl:
    def __init__(self, total_budget):
        self.total_budget = total_budget
        self.allocated = 0

    def allocate(self, amount):
        if self.allocated + amount <= self.total_budget:
            self.allocated += amount
            return True
        return False

    def release(self, amount):
        self.allocated = max(0, self.allocated - amount)

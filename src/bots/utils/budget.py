class BudgetManager:
    def __init__(self, initial_budget=100):
        self.budget = initial_budget
        self.expenses = []

    def spend(self, amount, desc=""):
        if self.budget - amount < 0:
            return False
        self.budget -= amount
        self.expenses.append((amount, desc))
        return True

    def add(self, amount, desc=""):
        self.budget += amount
        self.expenses.append((-amount, desc))

    def get_budget(self):
        return self.budget

    def history(self):
        return self.expenses

class AtmSimulation:
    def __init__(self):
        self.name = ""
        self.balance = 0.0
        self.history = []
        self.count = 0
    def create_account(self, name):
       
        if self.name:
            return False
        self.name = name
        if self.count < 10:
            self.history.append("Created account for " + name)
            self.count = self.count + 1
        return True
    def deposit(self, amount):
        if amount <= 0:
            return False
        self.balance = self.balance + amount
        if self.count < 10:
            self.history.append("Deposited " + str(amount))
            self.count = self.count + 1
        return True
    def withdraw(self, amount):
        if amount <= 0 or amount > self.balance:
            return False
        self.balance = self.balance - amount
        if self.count < 10:
            self.history.append("Withdrew " + str(amount))
            self.count = self.count + 1
        return True
    def get_history(self):
        result = []
        history = 0
        while history < self.count:
            result.append(self.history[historyIndex])
            history = history + 1
        return result
    def get_balance(self):
        return self.balance
    def get_name(self):
        return self.name
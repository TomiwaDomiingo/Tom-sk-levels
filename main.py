class Atm:
    def __init__(self):
        self.name = ""
        self.balance = 0.0
        self.history = []
        self.count = 0
    def create(self, name, start):
        if not name or start < 0:
            return False
        if self.name:
            return False
        self.name = name
        self.balance = start
        if self.count < 10:
            self.history.append("Created account for " + name + " with balance " + str(start))
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
        if amount % 500 != 0 and amount % 1000 != 0:
            return False
        self.balance = self.balance - amount
        if self.count < 10:
            self.history.append("Withdrew " + str(amount))
            self.count = self.count + 1
        return True
    def get_history(self):
        result = []
        i = 0
        while i < self.count:
            result.append(self.history[i])
            i = i + 1
        return result
    def get_balance(self):
        return self.balance
    def get_name(self
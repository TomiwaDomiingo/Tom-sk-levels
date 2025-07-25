class BankAccount:
    def __init__(self, name, number, withdraw):
        self.name = name
        self.number = number
        self.withdraw = withdraw
        self.balance = 1000 - self.withdraw

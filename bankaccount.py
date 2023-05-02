class BankAccount:
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
    
    def deposit(self, total):
        self.balance += total
        return self
    
    def withdraw(self, total):
        if total > self.balance:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5 
        else:
            self.balance -= total
        return self

    def display_account_info(self):
        print("Curent balance: $" + str(self.balance))
        return self

    def yield_interest(self):
        if self.balance > 0:
            int = self.balance * self.int_rate
            self.balance += int
            return self

account = BankAccount(.05, 1000)
account.deposit(100).deposit(100).deposit(100).withdraw(200).yield_interest().display_account_info()
# account.withdraw(1500).display_account_info()

account_2 = BankAccount(.05, 2000)
account_2.deposit(500).deposit(500).withdraw(100).withdraw(100).withdraw(100).withdraw(100).yield_interest().display_account_info()


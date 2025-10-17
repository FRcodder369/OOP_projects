
class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance


    def deposit(self, amount):
        self.balance += amount
        print(f'{self.name} deposited ${amount}. Current balance is ${self.balance}')


    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f'{self.name} withdrawn ${amount}. Current balance is ${self.balance}')
        else:
            print("You don't have enough funds")


class SavingsAccount(Account):
    def __init__(self, name, balance, interest_rate):
        super().__init__(name, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.deposit(interest)


account1 = Account('Alex', 1000)
account1.deposit(500)
account1.withdraw(200)
print()

saving_account = SavingsAccount('Alex', 2000, 0.05)
saving_account.deposit(1000)
saving_account.add_interest()
saving_account.withdraw(500)
saving_account.withdraw(1000)

            
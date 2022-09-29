class BankAccount:
    int_rate = 0.01
    balance = 0
    all_accounts = []

    def __init__(self, name, int_rate, balance):
        self.name = name
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)

    def deposit(self, amount):

        self.balance = self.balance + amount
        return self

    def withdraw(self, amount):

        if self.balance >= amount:
            self.balance = self.balance - amount
            return self
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance = self.balance - 5
            return self

    def display_account_info(self):
        print(f"Balance: ${self.balance} \n Interset Rate: {self.int_rate}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance = self.balance + (self.balance * self.int_rate)
            return self

    @classmethod
    def all_instances(cls):
        for account in cls.all_accounts:
            account.display_account_info()


user1 = BankAccount("user1", 0.02, 100)

user1.display_account_info()

user1.deposit(20).deposit(50).deposit(12).withdraw(100).display_account_info()

user2 = BankAccount("user2", 0.01, 200)

user2.display_account_info()

user2.deposit(50).deposit(100).withdraw(20).withdraw(100).withdraw(
    50).withdraw(90).display_account_info().yield_interest().display_account_info()

colby = BankAccount("Colby", 0.1, 1000)

BankAccount.all_instances()

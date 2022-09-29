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
        print(
            f"Account: {self.name} \n Balance: ${self.balance} \n Interset Rate: {self.int_rate}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance = self.balance + (self.balance * self.int_rate)
            return self

    @classmethod
    def all_instances(cls):
        for account in cls.all_accounts:
            account.display_account_info()


class User:
    def __init__(self, first_name, last_name, email, age, account_name, int_rate, balance):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.account = BankAccount(account_name, int_rate, balance)
        self.is_rewards_member = False
        self.gold_card_points = 0
        pass

    def display_info(self):
        print(self.first_name)
        print(self.last_name)
        print(self.email)
        print(self.age)
        print(self.is_rewards_member)
        print(self.gold_card_points)

    def enroll(self):
        if not self.is_rewards_member:
            self.is_rewards_member = True
            self.gold_card_points = 200
        else:
            print("User is already a member")

    def spend_points(self, amount):
        if self.gold_card_points >= amount:
            self.gold_card_points = self.gold_card_points - amount
        else:
            print("Not enough points")

    def make_deposit(self, amount):
        self.account.deposit(amount)

    def make_withdrawl(self, amount):
        self.account.withdraw(amount)

    def display_user_balance(self):
        print(f"{self.first_name}'s Balance is: ${self.account.balance}")

    def transfer_money(self, amount, other_user):
        if self.account.balance >= amount:
            self.account.balance = self.account.balance - amount
            other_user.account.balance = other_user.account.balance + amount
            return self.account.balance and other_user.account.balance
        else:
            print("Insufficient funds")
            return self.account.balance and other_user.account.balance


colby = User("Colby", "Leed", "colbyleed@yahoo.com", 35, "Checking", 0.1, 150)
leanne = User("LeAnne", "Leed", "leanneleed@gmail.com",
              37, "Savings", 0.2, 300)
luna = User("Luna", "Leed", "mstunaleed@yahoo.com", 0.5, "Savings", 0.5, 1500)

colby.account.display_account_info()
colby.make_deposit(100)

colby.display_user_balance()

colby.transfer_money(400, leanne)

BankAccount.all_instances()

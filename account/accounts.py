class Account:
    count = 1

    def __init__(self, name):
        self.name = name
        self.id = self.count
        self.account_num = '00093' + str(self.count)
        self.count += 1
        self.balance = 0.0

    def deposit(self, amount):
        if amount < 0:
            raise ValueError('Invalid amount')
        self.balance += amount

    def withdraw(self, amount):
        if self.balance - amount < 0:
            raise ValueError('Your account balance is low')
        self.balance -= amount

    def transfer(self, amount, account):

        if self.balance < amount:
            raise ValueError('Your account balance is low for this transfer')
        self.withdraw(amount)
        account.balance += amount







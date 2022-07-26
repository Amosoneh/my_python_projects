class Account:
    def do_this(self):
        print('From Account')


class Accounts(Account):
    def do_this(self):
        print('From Accounts')


class B(Account):
    def do_this(self):
        print('From C')


class C(Accounts, Account):
    def do_this(self):
        print('From C')


help(C)
print(C.__mro__)
print(C.mro())

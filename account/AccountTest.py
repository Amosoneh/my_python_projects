import unittest

from account.accounts import *


class MyTestCase(unittest.TestCase):

    def test_account_was_created(self):
        account = Account('Amos')
        self.assertEqual('Amos', account.name)  # add assertion here
        print(account.id)

    def test_deposit(self):
        account = Account('Amos')
        account.deposit(1000)
        self.assertEqual(1000, account.balance)

    def test_negative_deposit_raised_error(self):
        account = Account('Amos')
        with self.assertRaises(ValueError) as e:
            account.deposit(-2000)

    def test_withdrawal(self):
        account = Account('Amos')
        account.deposit(1000)
        account.withdraw(500)
        self.assertEqual(500, account.balance)

    def test_transfer(self):
        account = Account('Amos')
        account.deposit(1000)
        account2 = Account('Monday')
        account2.deposit(1000)
        account.transfer(500, account2)
        self.assertEqual(500, account.balance)


if __name__ == '__main__':
    unittest.main()

#!/usr/bin/env python3

#Q5. Banking System (Part 2). The bank introduces a new policy: when displaying the account balance using the get_balance() method, you must also include a message specifying the type of account (e.g., "Savings Account" or "Current Account") in the output.

#Update your code to implement this new feature.

#Consider the maintainability of the system: if the bank decides to add more account types in the future, you should be able to introduce the new account type without rewriting the balance logic.

class BankAccount:

    def __init__(self):
        self._account_number = None
        self._owner_name = None
        self._balance = 0
        self._active = True

    def deposit(self, value):
        self._balance += value

    def withdraw(self, value):
        if self._balance - value >= 0:
            self._balance -= value
        else:
            print('Insufficient Funds')

    def get_account_type(self):
        return 'Bank Account'

    def get_balance(self):
        return f'Account type: {self.get_account_type()}\nCurrent balance: ${self._balance:.2f}'

class SavingsAccount(BankAccount):

    def __init__(self):
        super().__init__()
        self.interst = 0.02

    def add_interest(self):
        self._balance *= self.interst

    def get_account_type(self):
        return 'Savings Account'

class CurrentAccount(BankAccount):

    def __init__(self):
        super().__init__()
        self.limit = -100

    def withdraw(self, amount):
        if self._balance - amount < self.limit:
            print(f'Over draft limit exeeded\nYou can only withdraw up to ${self._balance - self.limit}')
        else:
            self._balance -= amount

    def get_account_type(self):
        return 'Current Account'

ba = BankAccount()
sa = SavingsAccount()
ca = CurrentAccount()

ba.deposit(500)
print(ba.get_balance())
ba.withdraw(200)
print(ba.get_balance())
ba.withdraw(350)

sa.deposit(500)
print(sa.get_balance())
sa.add_interest()
print(sa.get_balance())

ca.deposit(500)
print(ca.get_balance())
ca.withdraw(550)
print(ca.get_balance())
ca.deposit(100)
print(ca.get_balance())
ca.withdraw(200)


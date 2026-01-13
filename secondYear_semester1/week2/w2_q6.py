#!/usr/bin/env python3

#Q6. Banking System (Part 3) The bank has introduced a policy where an interest rate applies to all types of accounts. For simplicity:

#SavingsAccount will have a 2% interest rate.
#CurrentAccount will have a 1% interest rate.

#You are required to implement a new method called apply_interest() that updates the account balance based on the interest rate. Ensure that the correct interest rate is applied to each account type.

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
        self.interest = 0.02

    def add_interest(self):
        self._balance *= self.interest

    def get_account_type(self):
        return 'Savings Account'

    def apply_interest(self):
        int = self._balance * self.interest
        self._balance += int

class CurrentAccount(BankAccount):

    def __init__(self):
        super().__init__()
        self.limit = -100
        self.interest = 0.01

    def withdraw(self, amount):
        if self._balance - amount < self.limit:
            print(f'Over draft limit exeeded\nYou can only withdraw up to ${self._balance - self.limit}')
        else:
            self._balance -= amount

    def get_account_type(self):
        return 'Current Account'

    def apply_interest(self):
        int = self._balance * self.interest
        self._balance += int

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
sa.apply_interest()
print(sa.get_balance())

ca.deposit(500)
print(ca.get_balance())
ca.withdraw(550)
print(ca.get_balance())
ca.deposit(100)
print(ca.get_balance())
ca.withdraw(200)
print(ca.get_balance())
sa.apply_interest()
print(ca.get_balance())


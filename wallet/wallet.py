class InSufficientFunds(Exception):
    pass


class Wallet(object):

    def __init__(self, balance=0):
        self.balance = balance

    def add_cash(self, amount):
        self.balance += amount

    def spend_cash(self, amount):
        if self.balance < amount:
            raise InSufficientFunds('Not enough Funds in your account {}'.format(amount))
        self.balance -= amount

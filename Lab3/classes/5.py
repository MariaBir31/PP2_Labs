
# Create a bank account class that has attributes owner,
# balance and two methods deposit and withdraw.
# Withdrawals may not exceed the available balance.
# Instantiate your class, make several deposits and withdrawals,
# and test to make sure the account can't be overdrawn.


class account:
    def __init__(self, balance, owner):
        self.balance = balance
        self.owner = owner

    def deposit(self, sum):
        self.balance = self.balance+sum

    def withdraw(self, sums):
        if sums > self.balance :
            print(f'Невозможно')
        else:
            print("Выведено")


s1 = account(1500, "Oleg")
s2 = account(1000, "Sasha")


s1.deposit(150)
s1.withdraw(1700)

s2.withdraw(999)
# Program: Bank Account System

# Demonstrate Encapsulation

class BankAccount:

    def __init__(self, balance):

        self.__balance = balance

    def deposit(self, amount):

        self.__balance += amount

        print(amount, "deposited successfully")

    def withdraw(self, amount):

        if amount <= self.__balance:

            self.__balance -= amount

            print(amount, "withdrawn successfully")

        else:

            print("Insufficient balance")

    def get_balance(self):

        print("Current Balance :", self.__balance)


account = BankAccount(5000)

account.get_balance()

account.deposit(1000)

account.withdraw(2000)

account.get_balance()


# Sample Output

'''
Current Balance : 5000

1000 deposited successfully

2000 withdrawn successfully

Current Balance : 4000
'''
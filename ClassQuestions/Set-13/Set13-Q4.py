class BankAccount:
    def __init__(self, account_number):
        self.__account_number = account_number
        self.__balance = 0

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient balance.")
        else:
            self.__balance = self.__balance - amount
            print(f"Updates balance is {self.__balance}")

    def deposit(self, amount):
        if amount <= 0:
            print("Please enter proper amount to deposit.")
        else:
            self.__balance += amount
            print(f"Updated balance is {self.__balance}")

    def display_balance(self):
        print(f"Balance for account number {self.__account_number} is {self.__balance}")



account1 = BankAccount(1234567890)
account2 = BankAccount(2581473690)

account1.deposit(10000)
account1.withdraw(5000)
account1.withdraw(6000)
account1.display_balance()

print()
account2.withdraw(500)
account2.deposit(1000)
account2.display_balance()
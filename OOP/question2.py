#encapsulation
class BankAccount:
    def __init__(self, __balance = 0):
        self.__balance = __balance

    def deposit(self, amount):
        print(f"current account balance is: {self.__balance}")
        print(f"you have deposited {amount}")
        self.__balance += amount
        return f"new account balance is: {self.__balance}"

    def withdraw(self, amount):
        print(f"You have withdrawn {amount} from the bank")
        self.__balance -= amount
        return f"remaining amount is: {self.__balance}"

account = BankAccount(100)
print(account.deposit(300))
print(account.withdraw(300))
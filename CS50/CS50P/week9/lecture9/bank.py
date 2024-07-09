# balance = 0


# def main():
#     print(f"Balance: {balance}")
#     deposit(100)
#     withdraw(50)
#     print(f"Balance: {balance}")

# def deposit(amount):
#     global balance
#     balance += amount

# def withdraw(amount):
#     global balance
#     balance -= amount


# if __name__ == "__main__":
#     main()

class Account():
    def __init__(self):
        self._balance = 0

    @property
    def balance(self):
        return self._balance
    
    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        self._balance -= amount

def main():
    account = Account()
    print(f"Balance: {account.balance}")
    account.deposit(100)
    account.withdraw(50)
    print(f"Balance: {account.balance}")

if __name__ == "__main__":
    main()
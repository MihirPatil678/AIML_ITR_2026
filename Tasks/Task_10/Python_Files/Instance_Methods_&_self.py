class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance
 
    def deposit(self, amount):
        self.balance += amount
        print("Deposited: Rs.", amount)
        print("New Balance: Rs.", self.balance)
 
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn: Rs.", amount)
            print("Remaining Balance: Rs.", self.balance)
        else:
            print("Insufficient Balance! Available: Rs.", self.balance)
 
    def show_balance(self):
        print("Account: ", self.account_holder)
        print("Balance: Rs.", self.balance)
 
acc = BankAccount("Mihir", 1400)
acc.show_balance()
acc.deposit(500)
acc.withdraw(300)
acc.withdraw(2000)   # Should Fail -> Insufficient Balance
acc.show_balance()
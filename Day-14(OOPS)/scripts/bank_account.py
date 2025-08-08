# 2. Model a BankAccount class with deposit(), withdraw(), and check_balance() methods.
class BankAccount:
    
    def __init__(self,account_no,balance):
        self.account_no = account_no
        self.balance    = balance
        
    def deposit(self,amount):
        self.balance = self.balance + amount
        
    def withdraw(self,amount):
        self.balance = self.balance - amount
        
    def check_balance(self):
        return self.balance

#! Bank Account Assignment

class BankAccounts:
    accounts = [] #? empty account
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        BankAccounts.accounts.append(self) #? BankAccount > empty account > instance


    def deposit(self,amount):
        self.balance += amount #? += because we are adding to the account
        return self

    def withdraw(self,amount):
        if(self.balance - amount) >= 0:
            print("insufficient funds:charging 5 dollars") #? referencing the balance instance here.
            self.balance -= amount #? this is for the actual withdraw
        return self


    def display_account_info(self):
        print(f"balance: {self.balance}") #? printing total balance
        return self


    def yield_interest(self):
        if self.balance > 0: #? balance must be over $0.00
            self.balance += (self.balance * self.int_rate) #? balance multiplied by the interest rate we pass | will only return if the balance is positive
        return self 

#? return self to execute

account_1 = BankAccounts(.02, 400)
account_2 = BankAccounts(1, 2000)
account_3 = BankAccounts(0.5, 10)

#? Make three deposits and one withdrawl + interest + account info
#? Make two deposits and four withdrawls + interest + account info
account_1.deposit(60).deposit(25).deposit(30).withdraw(700).yield_interest().display_account_info()

account_2.deposit(770).deposit(600).withdraw(40).withdraw(20).withdraw(100).withdraw(201).yield_interest().display_account_info()

account_3.deposit(10).withdraw(5).deposit(199).yield_interest().display_account_info()
#?Use chain method to keep DRY

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccounts(int_rate=0.02, balance=0)
    
    # other methods
    
    def make_deposit(self, amount):
        self.amount = amount



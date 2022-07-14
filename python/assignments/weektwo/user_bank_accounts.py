
#! Bank Account class
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

#! User class

class User:
    def __init__(self, user_name):
        self.user_name = user_name
        self.account = BankAccounts(0.2, 500)

    def make_withdraw(self, amount):
        self.amount -= amount
        return self

    def make_deposit(self, amount):
        self.amount += amount
        return self

    def display_user_balance(self):
        print(f"user: {self.user_name} | balance: {self.account}")
        return self



harry = User("harry")

harry.account.deposit(100)
harry.display_user_balance()



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
        if(self.balance - amount) < 0:
            print("insufficient funds:charging 5 dollars") #? referencing the balance instance here.
            self.balance -= 5 #? this is for the insufficient funds penalty.
        else:
            self.balance -= amount
            print(f"Your new balance: {self.balance}")
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
        self.account = {
            "checking" : BankAccounts(0.5, 1500),
            "savings" : BankAccounts(0.5, 5000)
        }
#? account has all the functionality and attributes of your bank account instance
    def make_withdraw(self, amount,account_name):
        self.account[account_name].withdraw(amount)#?self is user >going into account> further into dictionary(bank account instance) > calling withdraw method
        return self

    def make_deposit(self, amount, account_name):
        self.account[account_name].deposit(amount)
        return self

    def make_transfer(self, amount, transfer_to_other_user, from_account, to_account):
        # self.account[from_account].withdraw(amount) #?could do either or.
        self.make_withdraw(amount, from_account)
        transfer_to_other_user.make_deposit(amount, to_account)

    def display_user_balance(self):
        print(f"user: {self.user_name} | checking balance: {self.account['checking'].balance} | savings balance: {self.account['savings'].balance}")
        return self



harry = User("harry")
hermoine = User("hermoine")

# harry.account.deposit(100)
# harry.display_user_balance()
# harry.make_withdraw(300)
# harry.make_deposit(1000)

harry.make_transfer(30,hermoine,"savings", "checking")
harry.display_user_balance()
hermoine.display_user_balance()



#!CLASS VS INSTANCE
#* We're now accustomed to designating instance attributes inseide the constructor, the __init__() method. Now we can "
# * also declare and set attributes that don't belong to a single instance but to the class itself. Likewise, noramlly when we create a method on a
# * class we pass in self to refer to the instance of the object. THese normal methods are reffered to as INSTANCE METHODS. But there are other types
# *of methods we can implement on a class. Methods that belong to the CLASS and not the INSTANCE"

#!Class attributes 
#* Are defined outside of any instance methods, and is shared among all instances of the class.
# class BankAccount:
#     #*Declaring a class attribute
#     #*shared among all bank accounts
#     bank_name = "First National DOjo"

#     def __init__(self, int_rate, balance):
#         self.int_rate = int_rate
#         self.balance = balance

#*class attributes are more flexible because we can change them on an instance or the entire class.

# #* changing them on an instance:
# adriensAccount = BankAccount()
# saidesAccount = BankAccount()
# adriensAccount.bank_name = "Dojo Credit Union"

# BankAccount.bank_name = "Bank of Dojo"

# print(adriensAccount.bank_name)
# print(saidesAccount.bank_name)

#! @classmethod

#* class smethods are defined with a decorator @classmethod. They belong to the class iself "
# * instead of the instance. Instead of implicitlly passing self into the method we pas cls. This 
# * is reference to the class"

class BankAccounts:
    banks_name = "Dojo money bank"
    #*new class attribute - a list of all accounts
    all_accounts = []

    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance 
        BankAccounts.all_accounts.append(self)
        #*class method to change the name of the bank

    @classmethod
    def change_bank_name(cls,name):
        cls.bank_name = name
        #*class method to get balance of all accounts

    @classmethod
    def all_balances(cls):
        sum = 0
        #*we use cls to refer to the class
        for account in cls.all_accounts:
            sum+= account.balance
        return sum

#? it's important to note that class methods have no access to the instance attriute or any attribute that starts with self. 

#! @staticmethod
#* static methods are functions defined within the class with a decorator @staticmethod. They have no access on instance or class "
# * attributes so if we need any existing values they need to be passed in as arguments
# 
# *if we want our BankAccounts class to have a utility function to add or subtract we could implement the @staticmethod on the class"

class BankAccountss:
    #*__init__ goes here
    def with_draw(self,amount):
        #* we can use the static method here to evaluate
        #* if we can withdraw the funds without going negative
        if BankAccountss.can_withdraw(self.balance,amount):
            self.balance -= amount
        else:
            print("Insufficient Funds")
        return self
    #*static methods have no access to any attribute
    #*only to what is passed into it
    @staticmethod
    def can_withdraw(balance, amount):
        if (balance - amount) < 0:
            return False
        else:
            return True


#!Association between classes

#* Now created a user class and a bank account class let's create a relationship between them.
#* A user HAS a bank account, or , in OOP terms, there is an association between thse two classes. What this means is that
#* instead of keeping track of a balance directly in the User class, we'll encapsulate all the bank account info and associate a user with
#*a specific  instance of a bank account.

#* Assume each user has one account that starts with a 0$ balance and an insterest rate of 2%. Now instead of the user having a balance 
#*attribute, they will now hve an attribute type BankAccount. To create this relationship we can update our User's __init__ method to something
#* like this removing the account_balance attribute and addon an account attribute:

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)
        

#* ::NOTE:: the bankaccount class should be in the same file as the User class so the reference
#* to it is recognized. take a look into odularization if you feel the need to have the 2 classes in separate files.

#* we interact with this new attribute just as we do with previous attributes -- the only differnce is that we have
#*personally defined the functionality of this class we know the attributes and methods available to the account attribute
#* by looking at our BankAccount class

class User:
    def example_method(self):
        #* we can call the BankAccount instance's methods
        self.account.deposit(100)
        #*or access its attributes
        print(self.account.balance)
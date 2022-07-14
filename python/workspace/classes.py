#::CLASSES::

#Whenever we declare a variable, we are creating an instance of a class. FOr example, by declaring x = [1, 2, 3], x is an instance of a list. An instance is 
#simply an object that follows the pattern defined by its class. "
# 
# Class User:
# attributes:
#   first_name
#   last_name
#   age
# 
# methods:
#   birthday() -##increases age
#   say_greeting() -##says hello
# 
# 
# Classes are like blueprints four our custom objects. They aren't the actual objects, but a plan for what properties and functionalities 
# they may have. We can now create custom objects to suit the need of our web applications
# 
# Here's the syntax for creating a class that we want to call User:"

# class User:
#     pass # we will fill this shortly

#and here's how we create a new instance of our class:

# michael = User()
# anna = User()

#now we'll start fleshing out our classes with:

#attributes: characteristics shared by all instances of the class type
#methods: actions that an object can perform. A user in a banking applications for example may beed to be able to calculate age
#based on the user's birthday or open a new bank account associated with that user.

#::CONSTRUCTOR & ATTRIBUTES::

#When you sign up for an account on a wesite, your info as a user is saved to a database. We need a uniform way to always include the "
# same data (first name | last name | age | email | etc.. Similar to filling out a form at a Dr.'s office
# 
# FOr this, we use a constructor which is a function that contains instructions for making a new instance of a class. Like when you turn in comppleted
# medical forms to the receptionist. Python has a special function called the __init_ method. When called this method will designate some space in memory to store
# the user, and then assign the first name, lasst name and age by executing the lines below."
#declare a class and give it name User
# class User:
#     def __init__(self):
#         self.first_name = "Ada"
#         self.last_name = "Love"
#         self.age = 34
#::NOTE:: we will use the term method to refer to functions that specifically belong to a class. or functions that are defined inside the scope of a 
#class definition. For now we only have one method, the __init__ method.

#::MAKING INSTANCES::

#"By defining the user class, we've defined a new data type, User! In the same way we create different lists, or dictionaries, we can create and store
# many different users. We said that the __init__ method creates a user, but when and how does this method get 
# called to create new users?
# 
# User():::NOTE::
# 
# You can use the syntax Your_Class_Name() to create and then store a new instance of a class, in this case, User() to make
# and save a new user in memory but remember you'll need a variable to sstore it. 
# 
# ::NOTE:: User.py
#"
# class User:
#     def __init__(self):
#         self.first_name = "Ada"
#         self.last_name = "Love"
#         self.age = 34
# #Now that you have a class set up with a constructor
# #You can assign new variables to new users in the outer scope.
# user_ada = User()
# print(user_ada.first_name)

#in this eample we're just storing two strings and a number together in the variable user_ada. Similar to how a dictionary stores multiple pieces of 
#data in one place, they are stored as one data type, type User. And you will access them with dot-notation.


# class Cats:
#     def __init__(self):
#         self.color = "Grey and White"
#         self.age = 8
#         self.favoritefood = "chicharones"
#         self.sisters = 3

# user_kennedy = Cats()
# print(user_kennedy.color)
# print(user_kennedy.favoritefood)
#output White and Grey | chicharones

#::INTRO TO SELF::
#SELF is basically a placeholder for future instances, future users, like a blank form. When the line user_kennedy = user() is executed "
# in the example above, the __init__ method is called, like a patient handing in the clipboard to the receptionist. In this case, the self variable is
# referring to user_ada. This step is a bit like writing her name or patient number on an empty folder and sticking her info in ti to file away. If you 
# create another variable with ay user_blank = user(), the constructor is called again but this time self variable inside the constructor will refer
# to user_2 much like a different patient handing in their form.
# 
# "
# user_blake = Cats()
# print(user_blake.age) # because we have not given blake her own dictionary in the class, will default to the dictionary we have on file.

#::SETTING ATTRIBUTES::
#::NOTE:: _ INSTANCE ATTRIBUTES: "
# Let's build a new class for storing data about shoes for a shoe store management application. We want a shoe to have a brand,type, price and stock status.
# 
# Instance attributes are defined in the constructor, that special __init__ method, which is called when a new object is instantiated, in this case, 
# when a new type of shoes is added to inventory." 
#plants.py
#"latinname
#commonname
# genus
# lightreq
# waterreq
# instock
# price
# 


# class Plants:
#     def __init__(self):
#         self.latinname = "philodenron hederacium"
#         self.commonname = "heart leaf philodendron"
#         self.lightreq = "bright indirect"
#         self.waterreq = "Once every 7 days"
#         self.instock = True
#         self.price = 7.99
#         self.potsize = '4"'

# #The first parameter of an instance method within a class will be self and the instance "
# # attributes are also indicated by self. Self is a reference to the instance, not the class. In this case 
# # this particular plant not the generic plant class" Now we can create instances of Plants outside the cope of the class definition."

# maranta_plant = Plants()
# hoya_plant = Plants()

# #we can alo set the values for our instance' atributes:

# maranta_plant = 9.99
# print(maranta_plant)

# hoya_plant = 13.99
# print(hoya_plant)
#output 9.99 | 13.99

#::PASSING IN ARGUMENTS::"
# while we want every plant to have a price, genus etc. we don't want all of our shoes to have the same. Now we are going to pass in 
# arguments into the __init__ method to specify a plant's instance attributes
# 
# Even though we have 7 instance attributes, we only require input for 3 of them. When a particular plant instance is 
# created we should expect to receive specific values for the method attributes. We'll assume however that every plant starts
# with in stock set to true. Lets' adjust code to allow arguments to be passed in upon instantiation so
# we can customize all the attributes as soon as it get s created. 
# 
# "

# class Plant:
#     #now our method has 4 parameters (including self):
#     def __init__(self, genus, price, name):
#         self.genus = genus
#         self.price = price
#         self.name = name 
# # the status is set to true by default
    
# plt = Plant()

# philodendron_plant = Plant("philodendron", 10, "heart leaf")
# hoyas_plant = Plant("hoya", 16, "crimson princess")
# print(philodendron_plant.genus)
# print(hoyas_plant.genus)

#::METHODS::
#Lets add functionality to our class. Methods are just functions that belong to a class. This means that we can't call
#them independently as we have called functions. These methods must be called from an instance of a class.
#"Example, we want to get custom greetings for users like 'hellow my name is blah' we want to be able to call the
# method from the user instance using dot notation, because each user has a different name."
# blah.greeting()
# to be able to call on this method, it needs to exist. 

# class User:
#     def __init__(self, name, email):
#         self.name = name
#         self.email = email
#         #adding the greeting method
#     def greeting(self):
#         print(f"hellow, my name is {self.name}")
#         #don't forget that the first parameter must be self. Now that our method is written we can call it.

# blah = User('blah blah', 'blahblah@codingdojo.com')
# bladdyblah = User('bladyblah', 'bladyblah@codingdojo.com')

# blah.greeting()
# bladdyblah.greeting()

#::NOTE:: SELF
# The self parameter includes all the information about the "
# individual object that has called the method. How does it get passed in? Based
# onthe signature for the __init__ method, it requires 3 arugents. However, when we all on it, 
# we only pass in two. Likewise the greeting method requires one argument but we call it 
# with no arguments. What's happening here? because we arcalling on the method from the INSTANCE
# this is known as implicit passage of self. When we call on a method from an instance, the 
# meory addresssof that instance, along with all of its information(name, eamil b, balance) is passed in as self."

#::CHANGING SHOES WITHOUT METHODS::

#TAKE THE ON SALE functionality we want t o implement. What would that look like without writing any methods?
#This makes the code long and difficult to read. It is not DRY

# class Shoe:
#     #now our method has 4 parameters including self
#     def __init__(self, brand, shoe_type, price):
#         self.brand = brand
#         self.type = shoe_type
#         self.price = price
#         #the status is set to True by default
#         self.in_stock = True

#     def on_sale_by_percent(self, percent_off): #remember to create a new function name for a new instance (ie can't use __init__ twice)
#         self.price = self.price * (1 - percent_off)

# #create two shoe instances
# skater_shoe = Shoe("vans", "low top trainer", 59.99)
# dress_shoe = Shoe("clue", "flats", 29.99)

#::NOTE:: This section is not DRY
# #the skater shoe go on sale by 20%#
# skater_shoe.price = skater_shoe.price * (1 - 0.2)#
# # The dress shoes go on sale by 10% reduction:#
# dress_shoe.price = dress_shoe.price * (1 - 0.1)#
        
# # The skater shoes go on sale AGAIN by another 10%:#
# skater_shoe.price = skater_shoe.price * (1 - 0.1)#

# We can make all of this into one line of code using a method.

# skater_shoe.on_sale_by_percent(0.2)
# dress_shoe.on_sale_by_percent(0.5)
# print(dress_shoe.price)

#PLANT STORE

class Plantstore:
    def __init__(self, genus, light, water, price):
        self.genus = genus
        self.light = light
        self.water = water
        self.price = price

    def plant_sale(self, percent_off):
        self.price = self.price * (1 - percent_off)

maranta_plant = Plantstore("maranta", "med light", "1/week", 8.99)

philodendron_plant = Plantstore("philodendron", "bright indirect light", "1/week", 10.99)

maranta_plant.plant_sale(0.5)
philodendron_plant.plant_sale(.75)

print(maranta_plant.price)
print(philodendron_plant.price)
#DICTIONARIES "
#A DICTIONARY is another mutable sequence type that can store any number of Python obects. Including other sequence types. 
# dictionaries consist of pairs (called items) of keys and their corresponding values. 
# 
# ::NOTE::
# 
# - a dictionary is an unordered collection of objects.
# - values are accessed using a key (typically a string)
# - a dictionary can shrink or grow as needed.
# - the contents of dictionaries can be modified
# - dictionaries can be nested
# - sequence operations such as slice cannot be used with dictionaries.
# 
#::NOTE:: "
# KEYS VS INDEXES
# 
# KEYS:
# - KEYS ARE TYPICALLY STRINGS
# - KEYS ARE NOT IN ANY SORT OF ORDER, AS DICTIONARY VALUES ARE NOT STORED SEQUENTIALLY IN MEMORY
# DICTIONARIES ONLY HAVE KEYS
# 
# INDEXES:
# - INDEXES ARE ALWAYS INTEGERS.
# - INDEXES ARE ORDERED (LEAST TO GREATEST) AS LIST AND TYPLE VALUES ARE STORED SEQUENTIALLY IN MEMORY
# - DICTIONARIES DO NOT HAVE INDEXES
# 
# ::CREATING DICTIONARIES::
# 
# Creating a dictionary in Python is like creating another sequence. While lists are enclosed by brackets - [], and typles are enclosed
# by parenthesis -(), dictionaries are enclosed by braces {}. Below are a couple of techniques you'll find useful when building dictionaries.
# 
# LITERAL NOTATION"
# person = {"first": "Ada", "last" : "Lovelace", "age" : 35, "is_organ_donor": True}
# capitals = {} #create an empty dictionary

#::NOTE::"
# the keys in the example above are all strings, but the values are a variety of types. Generally you will only use strings for you
# keys. You can think of them as a label for the stored value.
# 
# ADDING NEW KEY-VALUE PAIRS:
# 
# -Dictionaries do not have a .append() method. You can add new values by setting a new key much like you would a  variable. "

# person = {"first": "Ada", "last" : "Lovelace", "age" : 35, "is_organ_donor": True}
# person_2 = {"first":"Adrian", "last" : "hatewool", "age": 53, "is_organ_donor": False}
# capitals = {} #create an empty dictionary and then add values
# capitals["svk"] = "Bratislava"
# capitals["deu"] = "Berlin"
# capitals["dnk"] = "Copenhagen"
# capitals["tko"] = "Tokyo"
# capitals["kyo"] = "Kyoto"
# print(capitals)

#in these examples above, we created two dictionaries in two different ways:

# 1. using literal notation. they key-value pairs are enclosed by curly brackets. The pairs are separated by commas. The first value of a pair is a 
# key which is followed by a colon and avalue. The "first_name" string is a key and the "ada" string is a value. 
#2. creating an empty dictionary and adding some values. They keys are inside the square brackets, the values are located on the right side of the assignment. 

# #::LIST SYNTAX::
# my_list[0] = 4

# #::DICTIONARY SYNTAX::
# my_dict["some_string"] = some_value

# ::DICTIONARY MANIPULATION::

# person = {"first": "Ada", "last": "Lovelace", "age": 42, "is_organ_donor": True}
# # Adds a new key value pair for email to person
# person["email"] = "alovelace@codingdojo.com"
        
# # Changes person's "last" value to "Bobada"
# person["last"] = "Bobada"
# # print(person)

# #::NOTE:: 
# #YOU CANNOT HAVE THE SAME KEY HAVING THE SAME NAME. IT WILL JUST REPLACE WHAT YOU HAD BEFORE.
# #TEST IT THIS SAY
# # if key not in dictionary: basically it's if some key is not in my dictionary update the value.

# if "email" not in person:
#     person["email"] = "newemail@email.com"
# else:
#     # print("Would you like to replace your existing email?")

#::CHALLENGE::
#keep track of how many times you've visited a country.
# countries_so_far = {"mexico" : 1, "canada" : 1}
# new_visits = {"taiwan" : 1, "japan" : 6}

# countries_so_far["korea"] = 1
# countries_so_far["mexico"] += 1

# print(countries_so_far)

#::ACCESSING VALUES::
#To access the values of a dictionary, you can use the familiar square brackets along with the key to obtain its value. 
# print(person["first_name"])
# full_name = person["first_name"] + " " + person["last_name"]

#::REMOVING VALUES::
# THERE ARE 2 WAYS TO REMOVE VALUES BELOW
# value_removed = capitals.pop('svk')
# del capitals['dnk']

#::MULTI-LINE SYNTAX TOO!::
# YOU CAN WRITE ANY DICTIONARYE'S KEYVALUE PAIRS ON MULTIPLE LINES TO MAKE IT EASIER TO READ.

#::COMMON BUILT-IN FUNCTIONS AND METHODS
# "len() - give the toal length of the dictionary
# str() - produces a string representation of a dictionary
# type() - returns the type of the passed variable. if passed variable is a dictionary it will return a dict type
# 
# HERE are some very useful python dictionary methods:
# .clear() - removes all elements from the dictionary
# .get(key, default=None) - a safe way to get a value, if the key might not exist. Returns the value for the specified key or None (ora value you
# specify if they key is not in the dicionary.
# .update(pairs_to_update) - add and update multiple key-value pairs at once by passing in another dictionary of the pairs to update and add. "

#::FOR LOOPS THROUGH DICTIONARIES::
#" Dictionaries are also iterable. When we iterate through a dictionary the iterator is each of the keys of the dictionary."
# my_dict = {"name":"me", "language":"js"}
    
# for each_key in my_dict:
#     print(each_key) 
    #output: name, language
#That means if we want the values of our dictionary, we might do something like this:
my_dict_2 = {"namey":"mine", "lang":"why"}
for each_one in my_dict_2:
    print(my_dict_2[each_one])
    #output:  mine, why

#dictionaries also have a few additional methods that allow us to iterate through them and have the keys and/or values as the iterator "
# test these out to get a better understanding"
capitals = {"Washington":"Olympia","California":"Sacramento","Idaho":"Boise","Illinois":"Springfield","Texas":"Austin","Oklahoma":"Oklahoma City","Virginia":"Richmond"}
# another way to iterate through the keys
for key in capitals.keys():
     print(key)
# output: Washington, California, Idaho, Illinois, Texas, Oklahoma, Virginia
#to iterate through the values
for val in capitals.values():
     print(val)
# output: Olympia, Sacramento, Boise, Springfield, Austin, Oklahoma City, Richmond
#to iterate through both keys and values
for key, val in capitals.items():
     print(key, " = ", val)
# output: Washington = Olympia, California = Sacramento, Idaho = Boise, etc

#::NESTED DICTIONARIES & LISTS
# Nesting is also allowed in dictionaries. In other words, dictionaries may contain list and tuples as well as other dictionaries. "
# Likewise lists may also contain dictionaries. All of these may be many levels deep. 
# "
# List of dictionaries
users = [
    {"first": "Ada", "last": "Lovelace"}, # index 0
    {"first": "Alan", "last": "Turing"}, # index 1
    {"first": "Eric", "last": "Idle"} # index 2
]
# Dictionary of lists
resume_data = {
    #        	     0           1           2
    "skills": ["front-end", "back-end", "database"],
    #                0           1
    "languages": ["Python", "JavaScript"],
    #                0              1
    "hobbies":["rock climbing", "knitting"]
}
#ACCESSING VALUES IN NESTED DICTIONARIES
#to access a value in a nested data structure take a look at how you would access the first user's name
print(users[0]["last"]) #prints Lovelace
#first users[0] is the whole user dictionary stored at index 0, next you find the value stored at the key "last" where we finally get the raw value, "lovelace.
# 
# "
print(resume_data["skills"][1])
print(users[2]["first"])





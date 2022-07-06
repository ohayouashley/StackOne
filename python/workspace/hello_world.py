#PYTHON INTRO

# The python shell.  

# You can turn your terminal into a python shell by typing python3 into your terminal. Once activated 
# we can type some python code and see the results immediately. When we see >>> we know we're in the shell.

# try: 
# >>> 4 + 5
# >>> 31/2
# >>> x = 9
# >>> y = "hello"
# >>> x * y		# what do you expect this one to do??

# In order to exit the python shell enter exit() in the terminal.

# print("Hello World")

#Now run this in the terminal by running python3 hello_world.py This runs the code. Now lets add some variables

# x = "hello python"
# print(x)
# y = 42
# print(y)

# #::PASS example::
# class EmptyClass:
#     pass

# # for val in my_string:
# #     pass

# #tuples

# dog = ('bruce', 'cocker spaniel', 19, False)
# # print(dog[0])
# dog[1] = 'dachshund' #error (on purpose) 'tuple' object does not support item assignment 
###########

# empty_list = []
# ninjas = ['Rozen', 'KB', 'Oliver']
# print(ninjas[2]) 	# output: Oliver
# ninjas[0] = 'Francis'
# ninjas.append('Michael')
# print(ninjas)	# output: ['Francis', 'KB', 'Oliver', 'Michael']
# ninjas.pop()
# print(ninjas)	# output: ['Francis', 'KB', 'Oliver']
# ninjas.pop(1)
# print(ninjas)	# output: ['Francis', 'Oliver']

# empty_dict = {}
# new_person = {'name': 'John', 'age': 38, 'weight': 160.2, 'has_glasses': False}
# new_person['name'] = 'Jack'	# updates if the key exists, adds a key-value pair if it doesn't
# new_person['hobbies'] = ['climbing', 'coding']
# print(new_person)	
# # output: {'name': 'Jack', 'age': 38, 'weight': 160.2, 'has_glasses': False, 'hobbies': ['climbing', 'coding']}
# w = new_person.pop('weight')	# removes the specified key and returns the value
# print(w)		# output: 160.2
# print(new_person)	
# output: {'name': 'Jack', 'age': 38, 'has_glasses': False, 'hobbies': ['climbing', 'coding']}        

# print(type(2.63))		# output: <class 'float'>
# print(type(new_person))		# output: <class 'dict'>
# print(len(new_person))		# output: 4 (the number of key-value pairs)
# print(len('Coding Dojo'))	# output: 11 


#view object type - use to figure out the type of any object

# print(type(24))
# print(type(3.9))
# print(type(3j))

#conversions

# int_to_float = float(35)
# float_to_int = int(44.2)
# int_to_complex = complex(35)
# print(int_to_float)
# print(float_to_int)
# print(int_to_complex)
# print(type(int_to_float))
# print(type(float_to_int))
# print(type(int_to_complex))

# import random
# print(random.randint(2,5)) # provides a random number between 2 and 5

# #string concatenation way one
# name = "Zen"
# print("My name is", name)

# #string concatenation way two
# name = "Zen"
# print("My name is " + name)

# #type casting or explicit type conversion

# #type casting
# print('hello' + 42)
# print('hello' + str(42))

# string interpolation: here we can disguise the user_val as an integer to be able to concatenate them.
# total = 30
# user_val = "13"
# # total = total + user_val
# total = total + int(user_val)

# print(total)

#f -strings
first_name = "dude"
last_name = "bro"
age = 36
print(f"my name is {first_name} {last_name} and I am {age} years old.")

#here's another way to do this using string.format
first_name = "Zen"
last_name = "Coder"
age = 27
print("My name is {} {} and I am {} years old.".format(first_name, last_name, age))
# output: My name is Zen Coder and I am 27 years old.
print("My name is {} {} and I am {} years old.".format(age, first_name, last_name))
# output: My name is 27 Zen and I am Coder years old.



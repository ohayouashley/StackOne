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

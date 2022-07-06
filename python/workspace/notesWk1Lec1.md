<!-- # PRIMITIVE DATA TYPES: STRINGS NUMBERS INT FLOAT BOOLEAN


# age = 5
# age_2 = '5'
# isOldEnough = True #capitalize t in True
# isTurnedOn = False #making sure you're being specific babout the naming convention
# isValid = True

# # for book in books:

# # for i in range(15):

# #python will infer what it is if you tell it something (line 4)

# #what happens when you add age 1 and age2

# print(age + age_2)

#composit data types: dictionary, list, tuples,
#list

# groceries = ['apples', 'peaches', 'bananas']

# print(groceries[0])


# sizes = [3, 5, 4, 6]

# print(sizes[0])

# real_groceries = [
#     {'apples' : 12}
# ]

# from multiprocessing.sharedctypes import SynchronizedString


# better_gorcery_list = {
#     'apples' : 12,
#     'pears' : 5,
#     'banana' : 4
# }

# print(better_gorcery_list['apples'])

player = {
    'name' : 'ashley',
    'age' : 30,
    'income' : 'lacking'
}

# print(player['name'])

# #tuple - immutable cannot be modified
# #form data you don't want ot be changed

# yes = ('yes', 'si', 'hai', 'da')

# russian_yes = yes[3]
#     print(player['age'])
#     print(player(sizes[0]))
#     print(Russian_yes)

# # concatenation

# print ( 'cat' + 'dog' )

# print('cat', 'dog')

# print('my age is' + 30)

# print('my age is', 36)


# print(f'my name is {player['name']}')

#conditionals

# temp = 91
# humidity = 60

# if temp > 100:
#     print("stay inside! It's scary hot out there")
# elif humidity < 65:
#     print("but it is a dry heat so it's ok")
# else:
#     print("let us go")

    ########


# car = """
#     Ferrari
# """

# print(car)

#loops

bikes = ['ducati', 'yamaha', 'ktm']

# for bike in bikes:
#     # print(bike)

# this way will cycle through the indecies (indexes)
#js
# for i in range(len(bikes)):
    #everything inside of the range () you're going to start at 0 and go until len (length) of bikes and increment by 1
# for i in range(0, len(bikes), 1):
#     #pass is something that you can use but you're not ready to use
#     print(bikes[i])

    # def add_numbers(): *not ready to add something so it wil break. pass just passes it up so that you can continue coding.
    #     pass

better_grocery_list = {
    'apples' : 12,
    'pears' : 5,
    'banana' : 4
}

for item in better_grocery_list:
    print(item,better_grocery_list[item]) -->

<!-- 
Python Fundamentals Basic Syntax & Indentation

::INDENTATION AND LINE ENDINGS::

WHAT IS A CODE BLOCK??

A code block is a det of lines of code that belog together. FOr example the first lkine of an if statement gives the condition
but the line(s) that follow explain what we want to happen if the condition is true.

Example:

def(functions)
if, elif, else (conditional statements)
for, while (loops)
class (classes)

Here the first line (containing the keyword) is not indented but ends with a colon :
The lines following that belong to that code block are indented 4 spaces
When the code block is over, indent back 4 spaces

x = 10
if x > 50:
    print("bigger than 50")
else:
    print("smaller than 50")

::PASS::

If we start a code blcok there must be at least one line of indented code immediately following. 
If we try to run a file with a hanging code block we'll get an error.
Using the pass statement we can continue coding until we need to without throwing an error.

The pass statement is a null operation; nothing happens when it executes.

::TYPES::

PRIMITIVE DATA TYPES

    NUMBERS, STRINGS, BOOLEANS
        FALSE IS 0 AND TRUE IS 1


    boolean values:
     -  assesses the truth value of something. It only has two values: true and false
         is_hungry = True
        has_braces = False
    
    number values:
     - intergers (whole numbers), floating point numbers (commonly known as decimal numbers, and complex numbers)
        age = 35 #storing an integer
        weight = 130.5 # storing a float
    *** There are 3 basic types of numbers in python. int (integers whole numbers positive or negative.)
        float (decimal numbers positive or negative)
        complets (ex. 1 +3j **note** if you're not sure if you need to use these it's safe to just ignore)
    
    string values:
        - literal text
        name = "joe schmoe"


COMPOSITE TYPES;
    LISTS, DICTIONARIES, TUPLES

        tuples:
            a type of data that is immutable ( cannot be modified after creation) and can hold a group of values. 
            Tuples can contain mixed data types.
            dog = ('bruce', 'cocker spaniel', 19, False)
            print(dog[0])
            dog[1] = 'dachshund'
        
        lists:
            a type of data that is mutable and can hold a gorup of values. Meant to store a collection of related data. 
            empty_list = []
ninjas = ['Rozen', 'KB', 'Oliver']
print(ninjas[2]) 	# output: Oliver
ninjas[0] = 'Francis'
ninjas.append('Michael')
print(ninjas)	# output: ['Francis', 'KB', 'Oliver', 'Michael']
ninjas.pop()
print(ninjas)	# output: ['Francis', 'KB', 'Oliver']
ninjas.pop(1)
print(ninjas)	# output: ['Francis', 'Oliver']

        dictionaries:
            a group of key-value pairs. Dictionary elements are indexed by unique keys which are used to access values.

COMMON FUNCTIONS
    PRINT(), LEN(), TYPE()

    print: print works pretty much the same as console.log in js. You can also use it to print out the types being used.
    print(type(2.63))		# output: <class 'float'>
    print(type(new_person))		# output: <class 'dict'>

    len: for data types that have a length attribute (eg. lists, dictionaryies, typles, stirngs), we can use
    the len function to get the length.
    print(len(new_person)) # output: 4 ( thenumber of the key-value pair)
    print(len('coding dojo')) #output: 11

::types::
if you are unsure on which type a number is you can use the type() to view the object type of any object;
print(type(24))
print(type(3.9))
print(type(3j))

::conversion::

all python objecs have data type methods we can use to convert number types from one to another.
int_to_float = float(35)
float_to_int = int(44.2)
int_to_complex = complex(35)
print(int_to_float)
print(float_to_int)
print(int_to_complex)
print(type(int_to_float))
print(type(float_to_int))
print(type(int_to_complex))

::random number::
python does not have a built in random number generator, use the random module instead.
import random
print(random.randint(2,5)) # provides a random number between 2 and 5


::STRINGS::
**string literals:  print("this is a sample")

::concatenating strings and variables with print::

- first way is to add a comma after the string followed by the variable. Note that the comma 
is outside of the closign quotation mark of the string. Print() punction inserts a space between elements separated by a comma.
name = "Zen"
print("My name is", name)
the second way is by concatenating the contents into a new string with the help of +
name = "Zen"
print("My name is " + name)
*try concatenating with an integer both of these ways. see what happens

::type casting or explicit type conversion::
if you want to change a value's data tyhpe from one type to another, python doesn't know how to add a string and a number
but it can add two strings together so if we can cast the number as a string then it will be able toadd the two
values together:
print("Hello" + 42)			# output: TypeError
print("Hello" + str(42))		# output: Hello 42

::f - strings (literal string interpolation)
Python 3.6 introduced f-stirngs for string interpolation. To consturct a f-string, place an f
right before the opening quotation. Then within the string, place any variables within curly brackets.
first_name: "dude"
last_name: "bro"
age = 36
print(f"my name is {first_name} {last_name} and I am {age} years old.")

::here's another way to do that using string.format
first_name = "Zen"
last_name = "Coder"
age = 27
print("My name is {} {} and I am {} years old.".format(first_name, last_name, age))
# output: My name is Zen Coder and I am 27 years old.
print("My name is {} {} and I am {} years old.".format(age, first_name, last_name))
# output: My name is 27 Zen and I am Coder years old.




>

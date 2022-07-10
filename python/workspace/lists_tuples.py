#::LISTS::

# Lists are comparable to arrays from abc import update_abstractmethods
# from crypt import methods
# from tkinter import INSIDE
# from JavaScript. 
# - indexed starting at 0
# - built in methods
# - defined with square brackets []
# - can store any data we want INSIDE
# - length can change - mutable

# A list (or an array) is a data type that allows you to hold groups of values. It's like a dresser
# with multiple drawers in which each drawer stores information. They are created with values inside 
# of square brackets [] where each value is separated by a comma. After a list is created it can be update_abstractmethodsby adding values and or bydeleting values.

# cats = ['kennedy', 'blake', 'knightly', 'birdie']
# grocery = [4, 'banana', 3, 'apple']
# empty_list = []

# fruits = ['apple', 'orange', 'banana', 'berries']
# veggies = ['broccoli', 'cauliflower', 'carrot', 'turnip']
# fruits_and_veggies = fruits + veggies
# # print(fruits_and_veggies)
# salad = 3 * veggies
# print(salad)

"""
::LIST MANIPULATION - lhs (left hand side) rhs (right hand side)

Think of a list as a drawer. We assign each drawer to a number [0]
drawers = ["documents", "envelopes", "pens"]

Setting values and accessing values. 
Drawers at 0 is a set value 
Whenever an index spot is on the lefthand side of the assingment operator, the value on the right hand side is going to replace whatever is in that drawer.
This is how you reassign a value to a particular array. L stands for lefthand side locations.

R stands for the righthand side location. 

Example: A

drawers = ["old erasers", "unused erasers", "new erasers"]

top_content = drawers[0] * in this instance, drawers[0] is going to replace what is hapening on the left hand side so



"""
#Example: A

drawers = ["old erasers", "unused erasers", "new erasers"]

# top_contents = drawers[0]

# top_contents = "unused erasers"

# print(drawers[0])
# print(drawers[1])
# print(drawers[2])

#replace "old erasers" with "mechanical erasers"

drawers[0] = "mechanical erasers"

# print(drawers)

#store the value of "mechanical erasers" in a temporary variable.

best_eraser = drawers[0]

drawers[1] = drawers[0]

# print(drawers)

# ::Left-hand-side vs right-hand-side::"
# 
# Whenevefr an inexed value in a list is on the right- side of the = assignment operator, the interpreter has to go
# fetch that raw value from memory. The left side is indicating the location in memory only, not the value.
# 
# Left side - location
# right side - value
# 
# ::APPENDING VALUES TO A LIST::
# 
# some_list.append(some_value)
# 
# the append method will append a new item onto the end of a given list. You can pass any data type into this function
# "

nums = [1,2,3,4,5]
nums.append(99)
# print(nums)

#:: SLICING:::"
# It's useful to know that python uses the following syntax: [:] to return a copy of some portion of the list, constrained by specified indices.
# This is called SLICING and it can be useful if you want to:1. use a copy of the list so you don't have to change the original 2. only use a 
# portion of a list.
# 
# The starting index and ending index should be separated by the : character
# 
# ::CHALLENGE::
# 
# READ EACH LINE OF THE CODE AND SEE F YOU CAN SEE THE PATTERN IN THE SYNTAX. WHAT DOES THE NUMBER BEFORE THE COLON DO
# WHAT ABOUT THE ONE AFTER, HOW ARE THEY DIFFERENT, WHAT IF THER IS NO NUMBER?
# "
          # 0       1      2     3     4
words = ["start","going","till","the","end"]
# print(words[1:]) #prints going till the end
# print(words[:4]) #prints start going till the
# print(words[2:4]) #prints till the
# print(words[:]) #prints everything "
# 
# Making a copy of a list
# "
copy_of_words = words[:]
copy_of_words.append("dojo") # only appends to the copy (meaning it will add to the end of the list)
# print(copy_of_words) #prints out the value of copy_of_words plus the appended dojo
# print(words) #will just print start going till the end.

#::BUILT IN FUNCTIONS FOR LISTS::"
# 
# There are built in functions that deal with lists. They can also be applied to all sequence types, including dictionaries,
# strings, and tuples. A sequence typ is anything over which we can iterate. Here's a common one:"
my_list = [1, 'zen', 'hi']
# print(len(my_list))
#output is 3 printing with len just prints out  the length of the array.

#::MORE FUNCTIONS TO USE WITH LISTS::"
# 
# 
# len(sequence) returns the length (number of items) in a sequence
long_list = [1,2,3,4,45,5,6,6,7,7,78,8,7,6,5,5,5,4,4,4,4,3]
# print(len(long_list))

# max(sequence) returns the highest value in a sequence"
# print(max(long_list))  #returns 78

#min(sequence) return the lowest value in a sequence
# print(min(long_list))

#sorted(sequence) returns a sorted sequence
# print(sorted(long_list))
#There are many other useful built-in functions.

#all() - will return if all items in an iterable are true, otherwise will return false.
# print(all(long_list))

# :: LIST SPECIFIC METHODS - DOT NOTATION::"
# 
# list.append(value) - appends a values to the end of the list "
# list.pop(index) removes a value at give position. If no parameter is passed it will remove the last value in the list
# list.index(value) - return the index (position) of given value if it exists in the list and raises error if it does not exist
# list.reverse() - reverses the order of the element in place
# list.sort() - sorts the items in order of least to greatest, or alphabetically for strings, in place
# ::**in place means it changes that same array, instead of returning a new array" 

#CHALLENGE B
some_nums = [44,56,2,3,12,19,6]
# print("Get started by writing your own code!")
#print the length of the list
# print(len(some_nums)) #return 7

#use another python built-in function and print the result
# print(min(some_nums)) returns 2
#remove an item from the list.
# print(some_nums.pop(3)) #return 3
# print(some_nums) # returns the array without 3

#utilize a method from the documentation and print the result
# print(sorted(some_nums))


#::TUPLES::
#"TUPLES ARE LIKE LISTS BUT THEY ARE IMMUTABLE. THEY ARE INDEXED STARTING AT 0 AND THEY ALSO HAVE BUILT IN METHODS. THEY 
# ARE DEFINED WITH () PARENTHESIS INSTEAD OF BRACKETS. WE CAN STORE ANY DATA WE WANT INSIDE. LENGTH IS FIXED WHICH MEANS YOU
# CANNOT ADD OR TAKE AWAY FROM A TUPLE 
# 
# A tuple is a container for a fixed sequence of data objects. The name comes from the latin suffix for multiples. They are 
#"sequences, just like lists. The difference is that they are immutable and they use parenthese. Creating a tuple is as simple as 
# declaring different comma-separated values. Optionally you can put these values between parenthesis
# 
# EXAMPLE:"
tuple_data = ('physics', 'chem', 2004, 2005)
tuple_num = (1,2,3,4,5)
tuple_letters = "a", "b", "c", "d"

#A tuple can be used to group any number of items into a single compound value. Syntactically, tuple is a comma separated sequence of values."
# although it is not necessary it is conventional to enclose tuples in parenthesis.
# 
# EXAMPLE"

dog = ("canis familiaris", "dog", "carnivore", 12)

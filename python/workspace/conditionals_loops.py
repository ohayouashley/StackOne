#::LOOPS::

#conditional statements allow us to run certain lines of code depending on whether certain conditions are met."
# These statements control the flow of how our code is executed by the interpreter. In Python, the keywords for conditional statements are
# if, elif, and else
# 
# Examples:"

# x = 12
# if x > 50:
#     print("bigger than 50")
# else: 
#     print("smaller than 50")
# because x is smaller than 50 the second print statement is the only one that will execute.

# y = 5
# if y > 10:
#     print("bigger than 10")
# elif y > 50:
#     print("bigger than 50")
# else: 
#     print("smaller than 10")

#even though y is smaller than 10 and 50 the first true statement is the only one that will execute,"
# so we will only see 'bigger than 10'"

# if y < 10:
#     print("smaller than 10")

#"::LOOPS:: 
# 
# -Sometimes we may want to iterate over a list or dictionary.  
# - default is to iterate by one
# 
# ::FOR LOOPS WITH range()
# 
# We can use the range function in conjunction with python for loops to repeat the same code as many times with a 
# number, usually called i that represents an integer that changes.
# this is similar to the loops in other languages by the syntax is different. The range() function can have between 1 and 3 arguments
# and creates a sequence of integers called a range object. 
# 
# ::THREE WAYS TO USE RANGE IN A LOOP
# 
# 1"

# for i in range(5):
    # print(i)

#"- i starts at 0 by default
# - exits loops when is 5
# (prints 4 but not 5)
# - i increases by 1 each time by defualt
# 
# 2. Two arguments"

# for i in range(2,7):
#     print(i)
#"- i starts at 2
# - exits when i is 7 (prints 6 but not 7!)
# - i increases by 1 each time by default
# 
# 3. Three arguments"

# for i in range(2,16,3):
#     print(i)
#"- i starts at 2
# - exits when i is 16 or larger than 16
# - i increases by 3 each time."

#Note that if  you need to specify an increment other than +1, all three arguments are required."
# You may also start at a large number and go down. To decrement the step will be a negative number to indicate i will get smaller
# with each iteration."

# for x in range(0,10,2):
#     print(x)
#prints 0 2 4 6 8

# for x in range(5,1,-3):
#     print(x)
#prints 5,2

# for x in range(1,21):
#     print(x)
#print all integers from  1-20 including 20

#::LOOPING OVER LISTS & STRINGS:: "
# 
# FOR LOOPS THROUGH STRINGS::
# 
# You can access each value of a string individually with a loop in a sequence"

# for x in 'Hello':
    # print(x) #output h, e , l , l , o

#FOR LOOPS THROUGH LISTS:
#IF WE WANT TO ITERATE THROUGH A LIST WE COULD USE THE RANGE FUNCTION AND SEND IN THE LENGTH OF THE "LIST
# AS THE STOPPING VALUE BUT IF WE ARE NOT INTERESTED IN THE INDEX VALUES AND WANT TO JUST SEE THE VALUES OF EACH ITEM IN THE "LIST
# IN ORDER, WE CAN LOOP TO GET THE VALUES OF THE LIST DIRECTLY!"

# my_list = ["abc", 123, "xyz"]
# for i in range(0, len(my_list)):
#     print(i, my_list[i])

# for v in my_list:
#     print(v)

#CHALLENGE:::

# countries = ["Uganda", "Chile", "Albania", "Saudi Arabia"]

# # Challenge 1: Fix the range!
# for i in range(0, 3):
#     # print(i)
#     # Challenge 2: print the index here
#     # print("countries: ", countries[0])
#     # Challenge 3: print the country here

# # Looping over values only...
# # for country in countries:
#     # print("Country: ")
#     # Challenge 4: print the country here

#     print(len(countries))


#::WHILE LOOPS::

#while loops are another way of looping while a certain condition is true.

#Here is a for loops and a while loop
#For loop:
for count in range(0,5):
    print("for looping =", count)

#While loop:
count = 0
while count <= 5:
    print("while looping - ", count)
    count += 1

#The basic syntax for a while loop loos like this: while<expression>:
#do something, including progress towards making the expression False. Otherwise it will never exit.

#:::ELSE::

#There are certain conditions that we give for every loop that we have, but twhat if they condition
#was not met and we still would like to do something if that happens? We can then use an 
#else statement with our while loop. 

# y = 3 
# while y > 0:
#     print(y)
#     y = y - 1
# else:
#     print("Finale else statement")

#::NOTE that this else code section is only eecuted if the while loops runs normally and its conditional is
# false (whether we never entered the while loop or we did but eventuallly the conditional is changed from
# #true to false). If instead our while loop is exited prematurely because ofa break or return statement then the else code section
#will never be executed.

#::LOOP CONTROL::
#We were introduced to control flow in the previous tabs with if and else statements. Loops, breaks, and 
#continues are all a part of control flow as well. When we want finer fontrol over your loops use the following statements:
#BREAK - the break statement exits the current loop prematurely, resuming execution at the first post-loop statement. The break "
# statement can be used in both while and for loops.
# 
# The most common use for the break is when some external condition is triggered, requiring a hasty exit from the loop."

for val in "string":
    if val == "i":
        break
    # print(val) #output: s,t,r - stops at i because thats where the break is.

#::CONTINUE::"
# THE CONTINUE STATEMENT IMMEDIATELY RETURNS CONTROL TO THE BEGINNING OF THE LOOP. In other words, the 
# continue statement rejects, or skips, all the remaining statements in the current iteration of the loop and continues
# normal execution at the top of the loop
# 
# The continue statement is useful when you want to skip specific iteration(s) but still keep going to the end."

for val in "string":
    if val == "i":
        continue
    # print(val) #out put s t r n g - skipped the i

y = 3
while y > 0:
    print(y)
    y = y - 1
    if y == 0:
        break
else:
    print("Final else statement")


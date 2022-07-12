#::INTRO TO FUNCTIONS

#Burger "
# - block of code to run at any point in program
# 0 can be defined and called anywhere in file
# - inside parenthesis are parameters - variables we can use in functions
# - call function those variables in paranthesis are called arguments
# - when we return something from function it becomes that  ie string, number etc
# 
# 
# A FUNCTION is a named block of code that we can execute to perform a specific task. It's a list of instructions that we can
# run any time and as many times as we want. 
# 
# All functions:
# 
# :: have names
# :: takes in parameters (parenthesis required, parameters optional
# :: perform a series of instructions
# :: return something afterwards ( will return Non if there is no explicit return statement)
# 
# Functions are like recipes they 
# - specify ingredients (variables) needed for the meal
# - use the actual ingredients (pass arguments) when starting (invoke a function)
# - follow the instructions step by step y (function) for the ingredients(parameters) and 
# repair them
# - once the food is ready we serve it up to those that are eating. (return)
# 
# "
#Burger function
# #def burger is a function


# def burger(bun, meat, cheese, toppings):
#     #instructions or logic in our functions:
#     split bun in half
#     cook meat
#     place cheese on meat
#     add toppings on meat
#     place top bun over everything

#     #now we can serve up our burger
#     return prepared ingredients

# #this is where the burger actually gets made and pass in arguments into the function
# lunch = burger(sesame bun, ground beef, american cheese, [mayo, lettuce , bacon, onions])


#The def keyword signifies the declaration of a function. It indicates that the following code "
# is a function and assigns a name to that function, so we can call it later. Parameters are inputs the function is expecting an appear
# inside the parenthesis that follow the function name.
# 
# Here is a basic example:"
# def add(a,b):
#     x = a + b
#     return x
# #returns x but does not print in terminal because the function is not being called. Inside the parenthesis are any values (arguments) the 
# #function is expecting as input.
# #Here we are calling the add function, with the arguments 3 and 5
# new_val = add(3,5)
# print(new_val) # the result of the add function gets sent back to and saved into new_value, so the output is 8.


#::PARAMETERS AND ARGUMENTS

#We define the input of functions using parameters. Functions can have as many parameters as we need including 0. "Here we've defined the 
# say_hi function with one parameter called name:"
# def say_hi(name):
    # print("hi, " + name)

#now we can invoke this function by calling its name and passing in the correct number or arguments.

# say_hi('mike')
# say_hi('elle')
# say_hi('dustin')

#::What is the dif between a parameter and an argument. We define parameters, we pass in arguments into functions.

#::RETURNING VALUES::

#In many cases we want our function to return some sort of value that we can use later. It is important to remember: "a function call is 
# equal to whatever that function returns."

# def say_hi(name):
#     return "Hi " + name
# greeting = say_hi("mike") #the returned value from say)hi function gets assigned to the 'greeting' variable
# print(greeting) #output hi mike

#returning a value from a function allow us to store that value in a variable. 

# def add(a,b):
#     x = a + b
#     return x
# sum1 = add(4,6)
# sum2 = add(1,4)
# sum3 = sum1 + sum2

# print(sum3)

#:::RETURN ALSO MEANS exit & print statements are for debugging."
# 
# 1. SAVING VALUES: when you print something with print(), strictly speaking, it doesn't have any affect on
# your program. No data is saved or changed or passed anywhere else in the program. Print statements are primarily used for programmers to debug the code
# to see what's happening in the program. A RETURN statement may pass a value back to the outer scope after it's done running for the program to use.
# Exiting the function: reaching a return statement always means "EXIT THIS FUNCTION NOW" WHETHER OR NOT THERE IS MORE CODE. ANY REMAINING CODE WILL NOT BE RUN"

#DEFAULT PARAMETERS:: "
# If you want to allow some of the parameters to be optional to the caller of the function, we can set defaults. Example: This function below is to 
# take a name and a number and print "good morning {some_name}" to the terminal the given number of times. If no name or number is given,
# the name is blank and the number is 2 respectively.
# "

# def be_cheerful(name='', repeat=2):
#     print(f"good morning {name}\n" * repeat)
# # be_cheerful()
# # be_cheerful("tim")
# # be_cheerful(name="john")
# # be_cheerful(repeat=6)
# # be_cheerful(name="michael", repeat=5)
# be_cheerful(repeat=3, name='kb')

#::NOTE:: " - all the different ways we are able to call on this one function! Even though our function dines 2 parameters, if:"
# - no arguments are provided -- the defaults are used
# - one unnamed argument provided -- provided value is used as the value for the first time parameter, and the second parameter's default is used
# - one named argument provided -- provided value is used as the value of the paramter of the same name, and the other parameter's default value is used
# - both unnamed arguments provided -- values assigned to parameters in order (ie what we've been doing up to this point)
# - both named arguments provided -- vaues are assigned to associated parameter and then the order doesn't matter.
# "

#::DEBUGGING IN PYTHON::
#It's important to use print to help you debug your code.
#::NOTE THIS IS WRONG::
# def multiply(num_list, num):
#     for x in num_list:
#         x *= num
#     return num_list
# a = [2, 4, 10, 16]
# b = multiply(a,5)
# print(b)
#output: [2,4,10,16]

#in this section above we are trying to multiply the section of the previous assignment. 

#We can get information as to why this is not returning what we want by using print statements to display that data in the terminal.

# The first thing to do is to step through your code in the order it runs and try to figure out if there are any unknowns.

#Here's what happened in order:
#::NOTE THIS IS RIGHT::
def multiply(num_list, num): #don't go inside the function until the function is called.
    a = [2,4,10,16] 
    b = multiply(a,5) #NOW OUR FUNCTION EXECUTES. WHAT IS A FUNCTION CALL EQUAL TO?
    print(b) # AND THE RESULTING VALUE IS PRINTED.

#So first we tried to declare a function, second we instantiated a variable whose value is a list containing integers,last we print the "
# output of that function by calling it after a print statement"
# Now comes the first unknown. What is the input, and what do you expect as the out put. If you get unexpected results you should "
# work to eliminate all unkowns. Try inserting a print statement as the first line. Sometimes it's useful to insert a print just to be sure the 
# code is executing when we think it is."

# def multiply(num_list, num):
#     print(num_list, num)
#     for x in num_list:
#         x *= num
#     return num_list

# a = [2,4,10,16]
# b = multiply(a,5)

# print(b)

#"The output confirms that the code is doing what we've tested it for so far. Next prove that the next line runs as expected. 
# The line for x in num_list: indicates the start of a for loop. Confirm we're entering the loop and theat "x" contains the value we expect"

# def multiply(num_list, num):
#     for x in num_list:
#         x *= num
#         print(x)
#     return num_list
# a = [2,4,10,16]
# b = multiply(a,5)

# print(b)

def multiply(num_list,num):
    print(num_list, num)
    for x in num_list:
        print(x)
        x *= num
    return num_list
a = [2,4,10,16]
b = multiply(a,5)
print(b)
# output:
# >>>[2, 4, 10, 16] 5
# >>>2
# >>>4
# >>>10
# >>>16
# >>>[2, 4, 10, 16]

#basically you're using the print function on each significant part of your code to make sure everything is doing what you want it to.

def multiply(num_list,num):
    for x in range(len(num_list)):
        num_list[x] *= num
    return num_list
a = [2,4,10,16]
b = multiply(a,5)
print(b)
# output:
# >>>[10,20,50,80]

#here is the correct code.
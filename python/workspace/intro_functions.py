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

def add(a,b):
    x = a + b
    return x
sum1 = add(4,6)
sum2 = add(1,4)
sum3 = sum1 + sum2
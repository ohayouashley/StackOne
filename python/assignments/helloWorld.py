# 1. TASK: print "Hello World"
print( "hello world" )
# 2. print "Hello Noelle!" with the name in a variable
name = "Ashley"
print( "hello", "Ashley" )	# with a comma
print( "hello " + "Ashley" )	# with a +
# 3. print "Hello 42!" with the number in a variable
name = 4
print( "hello", 4 )	# with a comma
print( "hello" + 4 )	# with a +	-- this one should give us an error!
# 4. print "I love to eat sushi and pizza." with the foods in variables
fave_food1 = "okonomiyaki"
fave_food2 = "oyakudon"
print(f('I love to eat', {fave_food1}, 'and ', {fave_food2})) # with .format()
print("I love to eat {} and {}".format(fave_food1, fave_food2)) # with an f string


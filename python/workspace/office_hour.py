# #office hour 7.7.22
# def cipher( text, encoded = False, offset = 3 ):
#     SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ.?!,;:()[]'
#     if encoded == False:
#         offset = -offset
#     ciphered= ""
#     for character in text:
#         num = SYMBOLS.find(character.upper()) #returns index of the string for that letter
#         if num + offset >= len(SYMBOLS): #if index/num +3 is >= the length of symbols
#             num = num + offset - len(SYMBOLS) #still moves three spots but subtracting the length of the array and starting at the beginning
#             ciphered += SYMBOLS(num)
#     else:
#         num += offset
#         ciphered += SYMBOLS(num)
#     return ciphered

# # print(cipher('aat', True))
# print(cipher('cat', offset = 6, encoded=True, text = 'cat'))
# cipher()
# x = [1,2,3]
# print(x[-1]) #shortcut to getting the very last thing in an array or a string
##########################
# def means define the function
# def say_hello( name ):
#     print((f"hello {name}"))
# #printing not returning because you're not

# say_hello('david')

"""
#make a function that creates an object/dictionary with keys of name, age ,a nd money with a default for age and money
"""

# def create_dict( name, age, money = 140000 ): #keep positioning in mind. 
#     return {
#         'name' : name,
#         'age' : age,
#         'money' : money
#     }

# print(create_dict('Ashley', 30, ))
# print(create_dict(age=31))
# print(create_dict('Ahley', 13))

#data for next challenge

people = [
    {'name' : "bob",
     'height' : 4.5,
     'gender' : 'male',
     'money' : 140000,
     'age' : 35,
     'video_game_fav' : 'call of duty'
    },

    {'name' : "shelly",
     'height' : 5.7,
     'gender' : 'female',
     'money' : 170000,
     'age' : 30,
     'video_game_fav' : 'pokemon'
    }

]

def find_person( name, min_money ):
    found_persons = []
    for person in people:
        if person['name'] == name and person['money'] >= min_money:
            found_persons.append(person)
    return found_persons

# print(find_person('shelly', 30))

#find people whose money is at least twice their age.

def find_wealth():
    wealth_people = []
    for person in people: 
        if person['money'] >= person['age'] * 2:
            wealth_people.append(person)
    return wealth_people

# print(find_wealth())

# print(people[0]['age']) #finds the person's age in the dictionary based on the index

#print a sentence about each person with proper grammar and punctuation.

def talk_about_ballers():
    rich_people = find_wealth()
    for person in rich_people:
        print(f"{person['name']} is wealthy, having {person['money']}")

talk_about_ballers()

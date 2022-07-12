
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
     'money' : 30,
     'age' : 35,
     'video_game_fav' : 'pokemon'
    }

]

def find_person( name, min_money ):
    found_persons = []
    for person in people:
        print(person)
        if person['name'] == name and person['money'] >= min_money:
            found_persons.append(person)
    return found_persons

print(find_person('shelly', 30))

#find people whose money is at least twice their age.

# def find_wealth():
#     wealth_people = []
#     for person in people: 
#         if person['money'] >= person['age'] * 2:
#             wealth_people.append(person)
#     return wealth_people

# # print(find_wealth())

# # print(people[0]['age']) #finds the person's age in the dictionary based on the index

# #print a sentence about each person with proper grammar and punctuation.

# def talk_about_ballers():
#     rich_people = find_wealth()
#     for person in rich_people:
#         print(f"{person['name']} is wealthy, having {person['money']}")

# talk_about_ballers()
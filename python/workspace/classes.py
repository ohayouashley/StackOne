# class User:
#     def __init__(self)

        
        

#__init__ fucntion has specific task

#what is the difference between a class and an instance
#class: is like a model - variable : defines a set of objects
#instance: is 

#a class is a definition or a blue print .
#mammal class: warm blooded, hair, oxygen
#methods of the class is: tails, 
#class defines a thing : it gives structure. You need legs you need eyes, you need height weigh color. 
#if we're creating an instance of a dog, 
#dog is an instance of an animal. 

#LECTURE:

# class Dog: 
#     def __init__(self, breed, height, weight, name):
#         self.breed= breed
#         self.breed= height
#         self.breed= weight
#         self.breed= name #the class is going to pass itself into this.

# Bob = Dog('shitszhu', 5, 6, 'steven') #this is an instance of Bob

# print(Bob.breed)

#this address that printed out is <__main__.Dog at 0x10ef323b0> 
#it says this because it's on the main page (the page that we are running) 
#we have this thing called dog and this is an object 

# def __init__(self,data) #passing in entire object of a person.
#     self.id = 

class Person:
    all_people = []
    def __init__(self, data):
        self.id = data['id']
        self.id = data['name']
        self.id = data['height']
        self.id = data['gender']
        self.id = data['money']
        self.id = data['age']
        Person.all_people.append(self) #appending an instance of a person that was just created. 

    def pay_day(self, pay): #need to pas self in the function it has to be self, whoever is calling this 
        self.money += pay
        return self. #returns because the function runs what the function returns.

    @classmethod
    def print_all_name(cls):
        for this_person in cls.all_people:
            print(f"This person's name is " {this_person.name})


people = [
    {
        "id" : 1
        "name" : 'harry'
        "height" : 5.6
        "gender" : 'male'
        "money" : 200
        "age" : 40
    },
        {
        "id" : 2
        "name" : 'hermoine'
        "height" : 5.4
        "gender" : 'female'
        "money" : 500
        "age" : 35
    }
]

#

# for dictionary in people: # this list above
#     Person(dictionary) #creating an instance with that dictionary

for this_person in people:
    Person(this_person)

Person.print_all_name

mike = Person.all_people[0]
print(mike.money)
print (mike.pay_day(50).pay_day(10).name) #returns 100 bob 150 bob is the first person's name on the dictionary list.
print(mike.money)

#these people need to be able to do things. Let s create a method for pay day. It will be an instance method.
#it will only apply to the individual that got paid which makes it an instance method.



# Person.print_all_names()

# def sum(x,y):
#     return x + y 

# money = sum(5,6)
# print(money) #Money returns 11 so that means money = 11

# def sum(x,y):
#     return x + y 

# money = sum(sum(5,6), sum(3,3))
#money = 17
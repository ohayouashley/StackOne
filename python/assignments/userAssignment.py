#User Assignment

class User:

    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self. email = email
        self. age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

    def display_info(self):
        print("-------------------")
        print(f"first name {self.first_name}")
        print(f"last name {self.last_name}")
        print(f"email {self.email}")
        print(f"age {self.age}")
        print(f"rewards member {self.is_rewards_member}")
        print(f"gold card points {self.gold_card_points}")
        print('--------------------')

    def enroll(self):    
        self.is_rewards_member = True
        self.gold_card_points = 100

        if self.is_rewards_member:
            print("User already a member")
            return False    

    def spend_points(self,amount):
        self.gold_card_points= self.gold_card_points - amount



user_1 = User("Harry", "Potter", "hpotter@hogwarts.edu", 20)
print(user_1.first_name)
print(user_1.last_name)
print(user_1. email)
print(user_1.age)
print(user_1.is_rewards_member)
print(user_1.gold_card_points)

user_2 = User("Hermoine", "Granger", "hgranger@hogwarts.edu", 21)


user_1.spend_points(50)
user_1.enroll()

user_2.spend_points(80)
user_2.enroll()
print(user_2.first_name)
print(user_2.last_name)
print(user_2.email)
print(user_2.age)
print(user_2.is_rewards_member)
print(user_2.gold_card_points)

user_1.display_info()
user_2.display_info()

#! Office Hour

class Fighter:
    lighter_weight = []
    heavy_weight =  []
    special_considerations = []
    def __init__(self,data):
        self.name = data['name']
        self.height = data['name']
        self.weight = data['name']
        self.special_considerations = data['name']

@classmethod
def add_fighters(cls, arr):
    #?reverse array
    rejected_stats = []
    arr = reverse_array(arr) #?(this func reverses the array)set reverse_array(arr) to arr so that we know we're working with the reversed array
    for fighter_stats in arr: 
        if validate_fighter_stats(fighter_stats): #? validating figher stats
            place_fighter_into_weight_class(cls(fighter_stats)) #?If fighter stats validated return
        else:
            rejected_stats.append(fighter_stats) #? if stats rejected place in rejected stats array
    return rejected_stats 

            

fighters_stats = [
    {
        'name' : 'Bob',
        'height' : 5,
        'weight' : 5,
        'age' : 32,
    }, 
    {
        'name' : 'Tim',
        'height' : 5,
        'weight' : 5,
        'age' : 32
    }, 
    {
        'name' : 'Dan',
        'height' : 5,
        'weight' : 5,
        'age' : 32
    }, 
]





#? 1. reverse the array - we can use this to reverse a list to go back and forth. 
def reverse_array(arr):
    pass

#? 2. validate each dictionary | 3. use each valid dict to create an instance.
def validate_fighter_stats(dict): #?passing dict so that we know we need to pass dictionary.
    #? Return true or falls (whether or not fighters dictionaries are valid
    pass

#? make sure function name is a verb because functions do things. Variables are nounds
def place_fighter_into_weight_class(fighter):
    pass 

#* Collasal cave adventure - game 


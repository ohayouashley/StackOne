#NUMBER ONE - update values in dictionaries and lists
# x = [ [5,2,3], [10,8,9] ] 
# students = [
#      {'first_name':  'Michael', 'last_name' : 'Jordan'},
#      {'first_name' : 'John', 'last_name' : 'Rosales'}
# ]
# sports_directory = {
#     'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
#     'soccer' : ['Messi', 'Ronaldo', 'Rooney']
# }
# z = [ {'x': 10, 'y': 20} ]
# #1
# x[1][0] = 15
# print(x)
# #2
# students[0]['last_name'] = "bryant"
# print(students)
# #3
# sports_directory['soccer'][0] = "Andres"
# print(sports_directory)
# #4
# z[0]['y'] = 30
# print(z)

#NUMBER TWO - iterate through a list of dictionaries
#1. 
# students = [
#          {'first_name':  'Michael', 'last_name' : 'Jordan'},
#          {'first_name' : 'John', 'last_name' : 'Rosales'},
#          {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#          {'first_name' : 'KB', 'last_name' : 'Tonel'}
#     ]
# iterateDictionary(students) 
# # should output: (it's okay if each key-value pair ends up on 2 separate lines;
# # bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel

# def iterate_dictionary(student_list):
#     for i in range(0,len(student_list)-1):
#         output = ""
#         for key, val in student_list[i].items():
#             output += f" {key} - {value},"
#             print(output)

# iterate_dictionary(students)


#NUMBER THREE - get values from a list of dictionaries ::This is wrong :()
# def iterate_dictionary_2(key_name, some_list):
#     for i in range(0, len(some_list)):

#             for key,val in list[i].items():
#                 if key == key_name:
#                     print(val)

# iterate_dictionary_2("first_name", students)
# iterate_dictionary_2("last_name", students)

#NUMBER FOUR - ITERATE THROUGH A DICTIONARY WITH LIST VALUES
# dojo = {
#    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
#    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
# }

# def print_info(some_dict):
#     for key,val in some_dict.items():
#         print("---------")
#         print(f"{len(val)} {key.upper()}")
#         for i in range(0, len(val)):
#             print(val[i])

# print_info(dojo)
# output:
# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank
    
# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon


#::LISTS::

# Lists are comparable to arrays from abc import update_abstractmethods
# from crypt import methods
# from tkinter import INSIDE
# from JavaScript. 
# - indexed starting at 0
# - built in methods
# - defined with square brackets []
# - can store any data we want INSIDE
# - length can change - mutable

# A list (or an array) is a data type that allows you to hold groups of values. It's like a dresser
# with multiple drawers in which each drawer stores information. They are created with values inside 
# of square brackets [] where each value is separated by a comma. After a list is created it can be update_abstractmethodsby adding values and or bydeleting values.

# cats = ['kennedy', 'blake', 'knightly', 'birdie']
# grocery = [4, 'banana', 3, 'apple']
# empty_list = []

# fruits = ['apple', 'orange', 'banana', 'berries']
# veggies = ['broccoli', 'cauliflower', 'carrot', 'turnip']
# fruits_and_veggies = fruits + veggies
# # print(fruits_and_veggies)
# salad = 3 * veggies
# print(salad)

"""
::LIST MANIPULATION - lhs (left hand side) rhs (right hand side)

"""

def cipher( text, encoded = False, offset = 3 ):
    SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ.?!,;:()[]'
    if encoded == False:
        offset = -offset
        ciphered= ""
    for character in text:
        num = SYMBOLS.find(character.upper()) #returns index of the string for that letter
        if num + offset >= len(SYMBOLS): #if index/num +3 is >= the length of symbols
            num = num + offset - len(SYMBOLS) #still moves three spots but subtracting the length of the array and starting at the beginning
            ciphered += SYMBOLS(num)
    else:
        num += offset
        ciphered += SYMBOLS(num)
    return ciphered

cipher('aat', True)


    # else:
    #     deciphered = ""
    #     for character in text:
    #         num = SYMBOLS.find(character.upper())
    #         if num -  3 < 0 :
    #         num = num - 3 + len(SYMBOLS)
    #     deciphered += SYMBOLS(num)

# print(cipher('dog', False))

# print('FDWCDQGCKDW', True)
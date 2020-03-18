# Given an array of numbers, create a function called oppositeArray that returns an array of numbers that are 
# the additive inverse (opposite or negative) of the original. If the original array is empty, return it.

def opposite_list(numbers):
    return []  if len(numbers)==0 else [-x for x in numbers]

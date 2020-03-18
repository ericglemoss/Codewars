#@ Write a function count_of_heads(initial, n, swings), which will provide the current number of heads. initial is an initial quantity of heads, that Zmey had. n is a multiplier, 
# and swings is a number of times Alyosha stroke Zmey with a sword, until he understood it was meaningless.

import math
def count_of_heads(initial, n, swings):
    total =  initial    
    for num in range(1,swings+1):
        total = total - 1 + math.factorial(num)*n
    return total

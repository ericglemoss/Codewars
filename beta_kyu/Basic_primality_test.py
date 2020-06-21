# We'll start with a simple primality function. Create the function prime that returns true when the given input is prime, and false when it is composite. 
# All inputs will be positive integers. (Don't use any built in modules or methods to do this challenge....)


import math
def prime(n):
    root = math.ceil(math.sqrt(n))
    for i in range(2,root):
        if n%i == 0:
            return False
    return True

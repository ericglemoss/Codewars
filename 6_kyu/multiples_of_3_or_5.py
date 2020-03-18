# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.

def solution(number):
    t = [i for i in range(3,number,3)]
    f = [i for i in range(5,number,5)]
    m = [i for i in range(15,number,15)]
    return sum(t)+sum(f)-sum(m)

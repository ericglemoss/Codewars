A perfect power is a classification of positive integers:

In mathematics, a perfect power is a positive integer that can be expressed as an integer power of another positive integer.
# More formally, n is a perfect power if there exist natural numbers m > 1, and k > 1 such that mk = n.

Your task is to check wheter a given integer is a perfect power. If it is a perfect power, return a pair m and k with mk = n as a proof. 
# Otherwise return Nothing, Nil, null, NULL, None or your language's equivalent.

from math import log, sqrt
def isPP(n):
    n = int(n)
    if n < 4: 
        return None
    tmp = round(sqrt(n),6)
    if tmp == round(tmp):
        return [tmp, 2]
    for m in range(2,int(n/2)):
        k = round(log(n,m),6)
        if k == round(k):
            return [m, k]
    return None

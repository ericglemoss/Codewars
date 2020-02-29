# In this kata you will have to calculate fib(n) where:
# fib(0) := 0;
# fib(1) := 1;
# fin(n + 2) := fib(n + 1) + fib(n)

# Write an algorithm that can handle n up to 2000000.
# Your algorithm must output the exact integer answer, to full precision. Also, it must correctly handle negative numbers as input.


import numpy as np
def fib(n):
    if n >=0:    
        mat = np.matrix([[1,1],[1,0]], dtype=object)**n
        return mat[0,1]
    else:
        n = -n
        mat = np.matrix( [[1,1],[1,0]], dtype=object) ** n
        return (-1)**(n-1) * mat[0,1]

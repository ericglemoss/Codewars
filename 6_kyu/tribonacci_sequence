# As the name may already reveal, it works basically like a Fibonacci, but summing the last 3 (instead of 2) 
# numbers of the sequence to generate the next.

# Well, you may have guessed it by now, but to be clear: you need to create a fibonacci function that given a signature array/list, returns 
the first n elements -  signature included of the so seeded sequence.

# Signature will always contain 3 numbers; n will always be a non-negative number; if n == 0, then return an empty array.

def tribonacci(signature, n):
    if n == 0:
        return []
    elif n <=3:
        return [signature[i] for i in range(n)]
    else:
        tribo = signature + [None]*(n-3)
        for k in range(3,len(tribo)):
            tribo[k] = tribo[k-1] + tribo[k-2] + tribo[k-3]
        return tribo

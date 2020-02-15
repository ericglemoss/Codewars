
# You have to build a Xbonacci function that takes a signature of X elements - and remember each next element is the sum of the last 
# X elements  - and returns the first n elements of the so seeded sequence.



def Xbonacci(signature,n):  
    if n <= len(signature):
        return [signature[i] for i in range(n)]
    else:
        elem_sum = 0
        xbona = signature + (n-len(signature))*[None]
        for k in range(len(signature),n):
            for j in range(k-len(signature),k):
                elem_sum +=  xbona[j]
            xbona[k] = elem_sum
            elem_sum = 0
        return xbona

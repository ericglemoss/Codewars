# Professor Chambouliard hast just discovered a new type of magnet material. He put particles of this material in a box made of small boxes
# arranged in K rows and N columns as a kind of 2D matrix K x N where K and N are postive integers. He thinks that his calculations 
# show that the force exerted by the particle in the small box (k, n) is:

#v(k,n) = 1/k*(n+1)**2*k

# Task: calculate S(K,N) = SUM(k = 1 to K)[SUM(n = 1 to N)v(k,n)]

def doubles(maxk, maxn):
    u=0
    for k in range(1, maxk+1):
        for n in range(1, maxn+1):
            u += 1/(k*(n+1)**(2*k))
    return u

# Complete the solution so that it splits the string into pairs of two characters. 
# If the string contains an odd number of characters then it should replace the missing second character of 
# the final pair with an underscore ('_').


def solution(s):
    tmp = list(s)
    out = []
    if len(s)%2==0:
        for i in range(0,len(tmp)-1,2):
            out.append(tmp[i] + tmp[i+1])
        return out
    else:
        for i in range(0,len(tmp),2):
            if i == len(tmp)-1:
                out.append(tmp[i] + '_')
            else:
                out.append(tmp[i]+tmp[i+1])
        return out

# Complete the solution so that the function will break up camel casing, using a space between words.

# EXAMPLE: solution("camelCasing")  ==  "camel Casing"

def solution(s):
    tmp = [char for char in s]
    for letter in tmp:
        if letter.isupper():
            tmp[tmp.index(letter)] = ' '+tmp[tmp.index(letter)]
    return ''.join(tmp)

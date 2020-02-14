# In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.

def high_and_low(numbers):
    num = numbers.split()
    temp = []
    for char in num:
        temp.append(int(char))        
    maximum = max(temp)
    minimum = min(temp)
    numbers = "{} {}".format(maximum,minimum)
    return numbers

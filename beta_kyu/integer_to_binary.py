# Convert an integer number into binary 1's and 0's string! Dealing only with positive integers,
# the input number should be able to be converted to a binary string with a leading zero!

def int_2_bin(num):
    return '0{0:b}'.format(num) if num != 0  else '0'

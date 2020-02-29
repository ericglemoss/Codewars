# Create a RomanNumerals class that can convert a roman numeral to and from an integer value. 
# It should follow the API demonstrated in the examples below. Multiple roman numeral values will be tested for each helper method.

# Modern Roman numerals are written by expressing each digit separately starting with the left most digit and skipping any digit with a value of zero.
# In Roman numerals 1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC. 2008 is written as 2000=MM, 8=VIII; or MMVIII. 1666 uses each Roman symbol in descending order: 
# MDCLXVI.

# Examples:
# RomanNumerals.to_roman(1000)  should return 'M'
# RomanNumerals.from_roman('M') should return 1000


class RomanNumerals:
    def __init__(self):
        pass
    
    def to_roman(num):
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
            ]
        syb = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
            ]
        roman_num = ''
        i = 0
        while  num > 0:
            for _ in range(num // val[i]):
                roman_num += syb[i]
                num -= val[i]
            i += 1
        return roman_num
    
    
    def from_roman(s):
        roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        integer_val = 0
        for i in range(len(s)):
            if i > 0 and roman_values[s[i]] > roman_values[s[i - 1]]:
                integer_val += roman_values[s[i]] - 2 * roman_values[s[i - 1]]
            else:
                integer_val += roman_values[s[i]]
        return integer_val

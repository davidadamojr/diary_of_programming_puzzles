"""
Given a roman numeral, convert it to an Integer

Input is guaranteed to be within the range from 1 to 3999.

Leetcode problem: https://leetcode.com/problems/roman-to-integer/
"""


# @param roman_string a string representing a roman numeral
# @return a string representing the numeral as a decimal integer
def roman_to_integer(roman_string):
    alphabet = {'I': 1,
                'V': 5,
                'X': 10,
                'L': 50,
                'C': 100,
                'D': 500,
                'M': 1000}

    previous = None
    value = 0
    for i in range(len(roman_string) - 1, -1, -1):
        if previous and alphabet[roman_string[i]] < previous:
            value = value - alphabet[roman_string[i]]
        else:
            value = value + alphabet[roman_string[i]]
        previous = alphabet[roman_string[i]]

    return value


if __name__ == '__main__':
    print(roman_to_integer("VII"))
    print(roman_to_integer("IX"))

"""
Reverse digits of an integer

Example1: x = 123, return 321
Example2: x= -123, return -321

Leetcode problem: https://leetcode.com/problems/reverse-integer/
"""


def reverse_integer(number):
    """
    Things to consider:
    - If the integer's last digit is 0, what should the output be? i.e. cases such
    as 10, 100
    - The reversed integer might overflow. Assume the input is a 32-bit integer, 
    then the reverse of 1000000003 overflows. 
    - For this problem, assume that your function returns 0 when the reversed integer 
    overflows
    """

    is_negative = False
    if number < 0:
        is_negative = True

    absolute_number = abs(number)

    # one may use the integer_to_string.py method here
    reversed_string = str(absolute_number)[::-1]  # reverses a string
    reversed_int = int(reversed_string)

    if reversed_int > 2 ** 31:
        return 0

    if is_negative:
        reversed_int = reversed_int * -1

    return reversed_int


if __name__ == "__main__":
    print(reverse_integer(123))
    print(reverse_integer(-123))
    print(reverse_integer(1000000003))

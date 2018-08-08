"""
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:
Input: 121
Output: True

Example 2:
Input: -121
Output: False
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore, it is not a palindrome.

https://leetcode.com/problems/palindrome-number/
"""


def is_palindrome_number(num):
    if num < 0:
        return False

    num_as_string = convert_integer_to_string(num)
    return is_palindrome_string(num_as_string)


def convert_integer_to_string(num):
    num_as_string = ""
    while num > 0:
        remainder = num % 10
        num = num // 10
        digit_as_string = chr(ord('0') + remainder)
        num_as_string = digit_as_string + num_as_string

    return num_as_string


def is_palindrome_string(num_as_string):
    return num_as_string == num_as_string[::-1]
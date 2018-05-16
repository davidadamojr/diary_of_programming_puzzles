"""
Given a non-negative number represented as an array of digits, plus one to the number.

The digits are stored such that the most significant digit is at the head of the list.

Leetcode problem: https://leetcode.com/problems/plus-one/
"""


def plus_one(digits):
    number_length = len(digits)
    number_value = 0
    for i in range(0, number_length):
        number_value = number_value * 10 + digits[i]

    plus_one = number_value + 1
    plus_one_str = str(plus_one)
    plus_one_str_list = list(plus_one_str)
    digit_list = [int(digit) for digit in plus_one_str_list]

    return digit_list


if __name__ == "__main__":
    print(plus_one([1, 2, 3, 4, 5]))
    print(plus_one([1]))
    print(plus_one([5, 4, 3, 2, 1]))

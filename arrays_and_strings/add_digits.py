"""
Given a non-negative integer "num", repeatedly add all its digits until the 
result has only one digit.

For example, 
Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only one 
digit, return it.

https://leetcode.com/problems/add-digits/
"""


def add_digits(num):
    if num < 10:
        return num

    digit_sum = 0
    while num != 0:
        digit = num % 10
        digit_sum = digit_sum + digit
        num = num / 10

    return add_digits(digit_sum)


if __name__ == '__main__':
    assert add_digits(38) == 2
    assert add_digits(1) == 1
    print("All test cases passed.")

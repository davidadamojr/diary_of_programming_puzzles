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


def is_palindrome(num):
    if num == 0:
        return True

    if num < 0 or num % 10 == 0:
        return False

    reversed_num = 0
    while num > reversed_num:
        reversed_num = reversed_num * 10 + num % 10
        num = num // 10

    return num == reversed_num or num == reversed_num // 10


assert is_palindrome(0) is True
assert is_palindrome(-10) is False
assert is_palindrome(1221) is True
assert is_palindrome(121) is True
print("All tests passed successfully.")

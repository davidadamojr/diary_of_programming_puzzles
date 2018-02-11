"""
Write a method that finds the maximum of two numbers. You should not use if-else or any other comparison operator.
"""

def sign(num):
    """returns 1 if num is positive and 0 if num is negative"""
    return ((num >> 31) & 0x1)

print bin(0x1)
assert sign(-10) == 0
assert sign(10) == 1

def max_number(num1, num2):
    pass

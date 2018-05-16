"""
Write a function to swap a number in place (that is, without temporary variables)
"""


def swap(a, b):
    # a is a number
    # b is a number
    print("Original value of a is " + str(a))
    print("Original value of b is " + str(b))
    a = a - b
    b = b + a
    a = b - a

    print("a is now " + str(a))
    print("b is now " + str(b))


swap(10, 12)
swap(-10, 12)

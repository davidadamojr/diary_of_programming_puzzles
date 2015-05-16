"""
Write a function to swap a number in place (that is, without temporary variables)
"""

def swap(a, b):
    # This solution works using XOR
    print "The original value of a is " + str(a)
    print "The original value of b is " + str(b)
    a = a ^ b
    b = a ^ b
    a = a ^ b
    print "The value of a is now " + str(a)
    print "The value of b is now " + str(b)

swap(10, 12)
swap(-10, 14)
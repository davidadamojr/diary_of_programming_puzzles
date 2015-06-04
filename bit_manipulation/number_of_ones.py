"""
Write a function that determines the number of 1 bits in the binary
representation of a given integer
"""
def number_of_ones(integer_value):
    """
    You can AND integer value with a "mask": 1
    This way, if the rightmost bit is 1, the result will be 1
    And if the rightmost bit is 0, the result will be 0
    Each time you do this, right shift one place so you can compare
    the next bit.
    O(n) - where n is the number of bits
    """
    original_value = integer_value
    one_count = 0
    while integer_value != 0:
        bit_is_one = integer_value & 1
        if bit_is_one:
            one_count = one_count + 1

        integer_value = integer_value >> 1

    print "The number of 1 bits in %d is %d" % (original_value, one_count)

def number_of_ones2(integer_value):
    """
    Another way to do this is to subtract 1 from the integer_value
    Doing this flips all the bits up to and including the rightmost 1.
    AND-ing the result of the subtraction and the original integer results
    in a new number that is the same as the original number except that the
    rightmost 1 is now a 0. Count the number of times you can do this before
    the number becomes 0.
    
    This is more efficient O(m) where m is the number of 1 bits
    """
    
    one_count = 0
    original_value = integer_value
    while integer_value != 0:
        one_subtracted = integer_value - 1
        integer_value = one_subtracted & integer_value
        one_count = one_count + 1

    print "The number of 1 bits in %d is %d" %(original_value, one_count)

number_of_ones(365)
number_of_ones2(365)


"""
Given a positive integer, print the next smallest and the next largest number 
that have the same number of 1 bits in their binary representation.
"""


def get_next_largest(number):
    one_count = 0
    zero_count = 0
    input_number = number

    # look past trailing zeros
    while input_number & 1 == 0:
        zero_count = zero_count + 1
        input_number = input_number >> 1

    while input_number & 1 == 1:
        one_count = one_count + 1
        input_number = input_number >> 1

    if one_count == 0 or input_number == 0:
        return number

    non_trail_zero_pos = one_count + zero_count
    mask = 1 << non_trail_zero_pos
    next_largest = number | mask

    # clear all bits up to the position of the first now-flipped non-trailing zero
    next_largest = next_largest & mask
    one_mask = 1 << (one_count - 1)
    one_mask = ~one_mask
    next_largest = next_largest | one_mask

    return next_largest


get_next_largest()

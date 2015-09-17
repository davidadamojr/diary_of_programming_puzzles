"""
Given a positive integer, print the next smallest and the next largest number 
that have the same number of 1 bits in their binary representation.
"""

# bit manipulation approach 

def get_next_number(integer_value):
    """
    - Flip the rightmost non-trailing zero bit at position p
    - rearrange all the bits to the right of p such that all zeros are on the right 
    and all ones are to the left.
    - Flip the rightmost 1 to a 0
    """
    
    number_of_ones = 0
    number_of_zeros = 0
    bit_value = integer_value
    
    while bit_value & 1 == 0 and bit_value != 0:
        number_of_zeros = number_of_zeros + 1
        bit_value = bit_value >> 1
    
    while bit_value & 1 == 1:
        number_of_ones = number_of_ones + 1
        bit_value = bit_value >> 1
        
    if bit_value == 0:
        return -1; # error
    
    rightmost_zero_pos = number_of_zeros + number_of_ones
    # flip the rightmost zero to a one
    integer_value = integer_value | (1 << rightmost_zero_pos)
    
    # clear all bits to the right of the rightmost zero position
    integer_value = integer_value & ~((1 << rightmost_zero_pos) - 1)
    
    # insert one less than the original number of ones to the right
    integer_value = integer_value | ((1 << (number_of_ones-1)) - 1)
    
    return integer_value

def get_previous_number(integer_value):
    """
    - count the number of trailing ones and the number of zeros immediately to 
    the left of the trailing ones
    - flip the rightmost non-trailing one to a zero at position p.
    - Clear all bits to the right of position p
    - insert one more than the number of trailing ones immediately to the right 
    of position p
    """
    bit_value = integer_value
    number_of_ones = 0
    number_of_zeros = 0
    
    while bit_value & 1 == 1:
        number_of_ones = number_of_ones + 1
        bit_value = bit_value >> 1
        
    if bit_value == 0:
        return -1 # error
    
    while bit_value & 1 == 0 and bit_value != 0:
        number_of_zeros = number_of_zeros + 1
        bit_value = bit_value >> 1

    # position of rightmost non-trailing one
    rightmost_one_pos = number_of_zeros + number_of_ones
    
    # clears from bit p onwards
    integer_value = integer_value & ((~0) << (rightmost_one_pos + 1))
    
    mask = (1 << (number_of_ones + 1)) - 1
    integer_value = integer_value | (mask << (number_of_zeros - 1))
    
    return integer_value
                            

if __name__ == '__main__':
    print get_next_number(52)
    print get_previous_number(52)
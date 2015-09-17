"""
Given a positive integer, print the next smallest and the next largest number 
that have the same number of 1 bits in their binary representation.
"""

# brute force solution that first counts the number of ones in the integer and 
# then continuously increments or decrements until it finds an integer with the  
# same number of ones

def get_next_smallest(integer_value):
    next_smallest = None
    number_of_ones = count_ones(integer_value)
    while integer_value != 0:
        integer_value = integer_value - 1
        if count_ones(integer_value) == number_of_ones:
            next_smallest = integer_value
            break
    
    return next_smallest

def get_next_largest(integer_value):
    next_largest = None
    number_of_ones = count_ones(integer_value)
    while integer_value != 0:
        integer_value = integer_value + 1
        if count_ones(integer_value) == number_of_ones:
            next_largest = integer_value
            break
    
    return next_largest

def count_ones(integer_value):
    number_of_ones = 0
    while integer_value != 0:
        if integer_value & 1 == 1:
            number_of_ones = number_of_ones + 1
        integer_value = integer_value >> 1
    
    return number_of_ones

if __name__ == '__main__':
    assert count_ones(get_next_smallest(52)) == count_ones(52)
    print get_next_smallest(52)
    
    assert count_ones(get_next_largest(52)) == count_ones(52)
    print get_next_largest(52)
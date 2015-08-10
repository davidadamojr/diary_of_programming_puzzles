"""
Write a method to randomly generate a set of n integers from an array of size 
n. Each element must have equal probability of being chosen.
"""

import random

# @param original_list list of n elements where m elements will be picked from
# @param number_of_elements list of elements to be picked
# @param m_index the index of the mth element in the array
def pick_elements(original_list, number_of_elements):
    subset = original_list[:number_of_elements]
    for i in range(number_of_elements, len(original_list)):
        random_number = random.randint(0, i)
        print random_number
        if random_number < number_of_elements:
            subset[random_number] = original_list[i]
        
    return subset

if __name__ == '__main__':
    original_list = [2,5,2,3,2,6,7,8,2,99,41]
    print pick_elements(original_list, 5)
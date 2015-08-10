"""
Write a method to randomly generate a set of n integers from an array of size 
n. Each element must have equal probability of being chosen.
"""

import random

# @param original_list list of n elements where m elements will be picked from
# @param number_of_elements list of elements to be picked
# @param m_index the index of the mth element in the array

def pick_elements(original_list, number_of_elements, current_index):
    if current_index == len(original_list):
        return original_list[:number_of_elements]
    
    if current_index >= number_of_elements:
        random_index = random.randint(0, current_index)
        if random_index < number_of_elements:
            original_list[random_index] = original_list[current_index]
    
    return pick_elements(original_list, number_of_elements, current_index+1)

if __name__ == '__main__':
    original_list = [11,2,34,5,2,23,53,2,2,3,55,24,66]
    print pick_elements(original_list, 5, 0)
        
    
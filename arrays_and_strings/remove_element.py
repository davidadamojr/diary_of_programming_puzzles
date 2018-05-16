"""
Given an array and a value, remove all instances of that value in place and 
return the new length.

The order of elements can be changed. It doesn't matter what you leave beyond 
the new length.

Leetcode problem: https://leetcode.com/problems/remove-element/
"""


# @param input_array a list of integers
# @param elem an integer value that needs to be removed
# @return an integer
def remove_element(input_array, elem):
    src_index = 0
    dst_index = 0
    while src_index < len(input_array):
        if input_array[src_index] != elem:
            input_array[dst_index] = input_array[src_index]
            dst_index = dst_index + 1

        src_index = src_index + 1

    return len(input_array[0:dst_index])


if __name__ == "__main__":
    print(remove_element([1, 2, 3, 1, 4, 5, 33, 2, 1], 1))

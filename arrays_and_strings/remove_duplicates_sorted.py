"""
Given a sorted array, remove the duplicates in place such that each element 
appears only once and return the new length

For example,
Given input array "nums = [1,1,2]",

Your function should return length = 2, with the first two elements of "nums" 
being 1 and 2 respectively. It doesn't matter what you leave beyond the new 
length. 
"""


# @param input_array list/array of integers
# @return an integer indicating the length of the new list/array
def remove_duplicates(input_array):
    # this could be implemented with a hash table requiring O(n) extra space
    # however, this solution avoids that and avoids the extra space complexity

    if len(input_array) == 0:
        return 0

    if len(input_array) == 1:
        return 1

    dst_index = 0
    src_index = 1
    while src_index < len(input_array):
        if input_array[src_index] == input_array[dst_index]:
            src_index = src_index + 1
        else:
            input_array[dst_index + 1] = input_array[src_index]
            dst_index = dst_index + 1
            src_index = src_index + 1

    return dst_index + 1


if __name__ == '__main__':
    print(remove_duplicates([1, 1, 2, 2, 3, 3, 3, 4, 5, 6]))

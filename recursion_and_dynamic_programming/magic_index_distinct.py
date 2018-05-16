"""
A magic index in an array A[1...n-1] is defined to be an index such that 
A[i] = i. Given a sorted array of distinct integers, write a method to find a magic 
index, if one exists, in array A.
"""


def find_magic_index(integer_list, start_index, end_index):
    """
    There is a linear time brute force solution which examines each element in 
    the list and checks to see if it is equal to its index. However, an approach 
    similar to binary search can be used to achieve O(log n) time complexity.
    
    This only works properly when the elements are distinct.
    """
    if end_index < 0 or start_index == len(integer_list):
        return None

    list_length = len(integer_list)
    middle_index = (start_index + end_index) / 2
    middle_element = integer_list[middle_index]
    if middle_element == middle_index:
        return middle_index
    elif middle_element < middle_index:
        return find_magic_index(integer_list, middle_index + 1, end_index)
    else:
        return find_magic_index(integer_list, start_index, middle_index - 1)


if __name__ == '__main__':
    integer_list = [-40, -10, 1, 3, 5, 7, 8, 9, 10, 10]
    print(find_magic_index(integer_list, 0, len(integer_list) - 1))

"""
A magic index in an array A[1...n-1] is defined to be an index such that 
A[i] = i. Given a sorted array of non-distinct integers, write a method to find a magic 
index, if one exists, in array A.
"""

def find_magic_index(sorted_array, start, end):
    """
    When the elements in the sorted array are non-distinct, then we need to 
    search both the left and right sides recursively
    """
    if sorted_array == [] or end < start or start < 0 or end == len(sorted_array):
        return None
    
    middle_index = (start + end) / 2
    middle_element = sorted_array[middle_index]
    if middle_element == middle_index:
        return middle_index
    
    # search right side
    rightIndex = max(middle_index + 1, middle_element)
    right = find_magic_index(sorted_array, rightIndex, end)
    if right:
        return right
    
    # search left side
    leftIndex = min(middle_index - 1, middle_element)
    left = find_magic_index(sorted_array, start, leftIndex)
    if left:
        return left 

if __name__ == '__main__':
    sorted_array = [-10, -5, 1, 2, 2, 6, 6, 7, 9, 12, 13]
    print find_magic_index(sorted_array, 0, len(sorted_array)-1)
    
    
"""
Given a sorted array of n integers that has been rotated an unknown number of times, 
write code to find an element in the array. You may assume that the array was originally 
sorted in increasing order.
"""


def find_in_rotated(key, rotated_lst, start, end):
    """
    fundamentally binary search...
    Either the left or right half must be normally ordered. Find out which 
    side is normally ordered, and then use the normally ordered half to figure 
    out which side to search to find x.
    """

    if not rotated_lst:
        return None

    if end < start:
        return None

    middle_idx = (start + end) / 2
    middle_elem = rotated_lst[middle_idx]
    leftmost_elem = rotated_lst[start]
    rightmost_elem = rotated_lst[end]

    if middle_elem == key:
        return middle_idx

    if leftmost_elem < middle_elem:
        if leftmost_elem <= key < middle_elem:
            return find_in_rotated(key, rotated_lst, start, middle_idx - 1)
        else:
            return find_in_rotated(key, rotated_lst, middle_idx + 1, end)
    else:
        if middle_elem < key <= rightmost_elem:
            return find_in_rotated(key, rotated_lst, middle_idx + 1, end)
        else:
            return find_in_rotated(key, rotated_lst, start, middle_idx - 1)


if __name__ == '__main__':
    assert find_in_rotated(1, [4, 5, 6, 1, 2, 3], 0, 5) == 3
    assert find_in_rotated(5, [1, 2, 3, 4, 5, 6], 0, 5) == 4
    assert find_in_rotated(5, [6, 6, 6, 6, 6, 6], 0, 5) == None
    assert find_in_rotated(7, [6, 6, 6, 7, 7, 7, 7], 0, 6) == 3
    assert find_in_rotated(6, [6, 6, 6, 6, 6, 6], 0, 5) == 2
    print("All test cases passed.")

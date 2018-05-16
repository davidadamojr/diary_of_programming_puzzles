"""
An iterative implementation of binary search
"""


def binary_search(sorted_list, key):
    low = 0
    high = len(sorted_list) - 1

    while low <= high:
        midpoint = (low + high) / 2
        middle_element = sorted_list[midpoint]

        if key > middle_element:
            low = midpoint + 1
        elif key < middle_element:
            high = midpoint - 1
        else:
            return "Key was found at position " + str(midpoint)

    return "Could not find element"


sorted_list = [1, 3, 4, 5, 6, 7, 33, 55, 66, 73]
print(binary_search(sorted_list, 3))

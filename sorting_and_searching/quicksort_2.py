"""
A not-very-space-efficient implementation of quicksort

This quicksort implementation is not stable
The best pivot selection is usually the one in the middle since it ensures
O(nlogn) time for sorted, mostly sorted and unsorted data

Recursion stops when a subset contains only one element
"""

def quicksort(unsorted_data):
    if len(unsorted_data) < 2:
        return unsorted_data

    data_length = len(unsorted_data)
    pivot_index = data_length / 2
    pivot_element = unsorted_data[pivot_index]

    less = []
    more = []

    for i in xrange(0, data_length):
        if i == pivot_index:
            continue

        element = unsorted_data[i]
        if element <= pivot_element:
            less.append(element)
        else:
            more.append(element)

    return quicksort(less) + [pivot_element] + quicksort(more)

print quicksort([2,5,3,2,7,20,3,12,13,88])


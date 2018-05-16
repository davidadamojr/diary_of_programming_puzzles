"""
Implement Insertion Sort

Insertion sort works by building a sorted array (or list) one element at a
time by comparing each new element to the already-sorted elements and inserting
the new element into the correct location

Insertion sort is a stable sorting algorithm
"""


def insertion_sort(unsorted_list):
    # the first item in the list is already trivially sorted
    list_length = len(unsorted_list)
    for i in range(1, list_length):
        j = i
        while j > 0 and unsorted_list[j - 1] > unsorted_list[j]:
            temp = unsorted_list[j - 1]
            unsorted_list[j - 1] = unsorted_list[j]
            unsorted_list[j] = temp
            j = j - 1

    return unsorted_list


print(insertion_sort([3, 2, 1, 4, 5, 2, 3, 5]))

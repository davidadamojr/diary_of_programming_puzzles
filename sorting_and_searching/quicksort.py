"""
Implement quicksort
- In quicksort, we pick a random element and partition the array such that all
numbers that are less than the partitioning element come before all elements
that are greater than it.
"""


def quicksort(unsorted_list, left, right):
    partition_index = partition_list(unsorted_list, left, right)
    if left < partition_index - 1:
        quicksort(unsorted_list, left, partition_index - 1)

    if partition_index < right:
        quicksort(unsorted_list, partition_index, right)


def partition_list(unsorted_list, left, right):
    # select the middle element to be the pivot
    pivot_element = unsorted_list[(left + right) / 2]

    while left <= right:
        while unsorted_list[left] < pivot_element:
            left = left + 1

        while unsorted_list[right] > pivot_element:
            right = right - 1

        if left <= right:
            unsorted_list[left], unsorted_list[right] = unsorted_list[right], unsorted_list[left]
            left = left + 1
            right = right - 1

    return left


if __name__ == '__main__':
    unsorted_list = [10, 8, 3, 2, 22, 34, 10, 32]
    quicksort(unsorted_list, 0, len(unsorted_list) - 1)
    print(unsorted_list)

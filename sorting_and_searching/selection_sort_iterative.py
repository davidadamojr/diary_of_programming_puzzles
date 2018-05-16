"""
An iterative implementation of selection sort - O(n^2)
"""


def selection_sort_iterative(data):
    data_length = len(data)
    if data_length == 0:
        return data

    for i in range(0, data_length):
        min_element_index = i
        for j in range(i + 1, data_length):
            # find minimum element
            if data[j] < data[min_element_index]:
                min_element_index = j

        # add the minimum element to the sorted part of the list
        data[i], data[min_element_index] = data[min_element_index], data[i]

    return data


print(selection_sort_iterative([2, 4, 67, 3, 7, 2, 5, 66, 20, 8]))

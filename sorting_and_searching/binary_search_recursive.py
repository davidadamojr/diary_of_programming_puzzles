def binary_search(sorted_list, left, right, key):
    midpoint = (left + right) / 2
    middle_element = sorted_list[midpoint]
    if middle_element == key:
        return "Key found at position: " + str(midpoint)

    if right <= left:
        return "Could not find element"

    if key < middle_element:
        return binary_search(sorted_list, left, midpoint-1, key)
    else:
        return binary_search(sorted_list, midpoint+1, right, key)


sorted_list = [1,4,5,5,6,7,8,9,22,43]
print binary_search(sorted_list, 0, len(sorted_list)-1, 22)

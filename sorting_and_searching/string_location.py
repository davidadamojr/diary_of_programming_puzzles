"""
Given a sorted array of strings which is interspersed with empty strings, write a method to find the location of
a given string.
"""

# @param string str the string to be located
# @param string str_lst list of strings interspersed with empty strings
def find_string_location(str, str_lst, start, end):
    if start > end or not str_lst or not str:
        return -1

    middle = (start + end) / 2

    middle_str = str_lst[middle]
    if middle_str == "":
        left = middle - 1
        right = middle + 1

        while True:
            if left < start and right > end:
                return -1

            if left >= start and str_lst[left] != "":
                middle = left
                break
            elif right <= end and str_lst[right] != "":
                middle = right
                break

            left = left - 1
            right = right + 1

    if str_lst[middle] == str:
        return middle
    elif str > middle_str:
        return find_string_location(str, str_lst, middle+1, end)
    elif str < middle_str:
        return find_string_location(str, str_lst, start, middle-1)

if __name__ == "__main__":
    assert find_string_location("danger", ["apple", "", "", "danger", "edible", "viscous", "", "zip"], 0, 7) == 3
    assert find_string_location("apple", ["apple", "", "", "danger", "edible", "viscous", "", "zip"], 0, 7) == 0
    assert find_string_location("zip", ["apple", "", "", "danger", "edible", "viscous", "", "zip"], 0, 7) == 7
    assert find_string_location("", ["apple", "", "", "danger", "edible", "viscous", "", "zip"], 0, 7) == -1
    print "All test cases passed successfully."

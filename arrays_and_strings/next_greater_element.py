"""
You are given two arrays (without duplicates) "nums1" and "nums2" where "nums1" is a subset of "nums2". Find all the
next greater numbers for the elements in "nums1" in the corresponding places of "nums2".

The next greater number of a number "x" in "nums1" is the first greater number to its right in "nums2". If it does not
exist, output -1 for this number.

Note:
1. All elements in "nums1" and "nums2" are unique.
2. The length of both "nums1" and "nums2" would not exceed 1000.
"""


def next_greater_element(nums1, nums2):
    stack = []
    next_greater_map = {}
    for num in nums2:
        while stack and stack[-1] < num:
            next_greater_map[stack[-1]] = num
            stack = stack[:-1]
        stack.append(num)

    next_greater_elements = []
    for num in nums1:
        next_greater_elements.append(next_greater_map.get(num, -1))

    return next_greater_elements


assert next_greater_element([2, 3], [1, 2, 3, 4]) == [3, 4]
assert next_greater_element([3, 2, 10], [1, 4, 2, 3, 6, 10]) == [6, 3, -1]
print("All test cases passed.")

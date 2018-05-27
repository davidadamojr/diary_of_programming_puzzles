"""
Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:
Input: [1,1,0,1,1,1]
Explanation: The first two digits or the last three digits are consecutive 1s.
The maximum number of consecutive 1s is 3.

Note:
- The input array will only contain 0 and 1.
- The length of input array is a positive integer and will not exceed 10,000
"""


def max_consecutive_ones(binary_nums):
    one_count = 0
    max_count = 0
    for num in binary_nums:
        if num == 1:
            one_count += 1
            if one_count > max_count:
                max_count = one_count
        else:
            one_count = 0

    return max_count

assert max_consecutive_ones([1, 1, 0, 1, 1, 1]) == 3
assert max_consecutive_ones([0, 0, 0, 0, 0, 0]) == 0
assert max_consecutive_ones([]) == 0
assert max_consecutive_ones([1, 1, 1, 1, 1, 1]) == 6
assert max_consecutive_ones([1]) == 1
assert max_consecutive_ones([0]) == 0
assert max_consecutive_ones([0, 0, 0, 1]) == 1
assert max_consecutive_ones([1, 0, 0, 0]) == 1
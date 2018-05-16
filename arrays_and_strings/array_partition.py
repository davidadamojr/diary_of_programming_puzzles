"""
Given an array of 2n integers, your task is to group these integers into n pairs of integers, say (a_1,b_1),(a_2,b_2)...,(a_n,b_n)
which makes sum of min(a_i,b_i) for all i from 1 to n as large as possible.

Example 1:

Input: [1,4,3,2]
Output: 4
Explanation: n is 2, and the maximum sum of pairs is 4 = min(1,2) + min(3,4).

Note:
    1. n is a positive integer, which is in the range of [1,10000].
    2. All the integers in the array will be in the range of [-10000,10000].
"""


def array_partition(nums):
    sorted_arr = sorted(nums)
    trailing_idx = 0
    leading_idx = 1
    sum = 0
    while leading_idx < len(nums):
        sum += min(sorted_arr[trailing_idx], sorted_arr[leading_idx])
        trailing_idx += 2
        leading_idx += 2

    return sum


if __name__ == "__main__":
    assert array_partition([1, 4, 3, 2]) == 4
    print("All tests passed successfully.")

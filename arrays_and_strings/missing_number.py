"""
Given an array containing n distinct numbers taken from 0,1,2,...,n. Find the one that is missing from the array.

Example 1:
Input: [3,0,1]
Output: 2

Example 2:
Input: [9,6,4,2,3,5,7,0,1]
Output: 8

Note:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?

Source: https://leetcode.com/problems/missing-number/description/
"""


def find_missing_number_1(nums):
    nums_set = set([])
    for num in nums:
        nums_set.add(num)

    for i in range(len(nums) + 1):
        if i not in nums_set:
            return i

    return None


def find_missing_number_2(nums):
    n = len(nums)
    n_sum = (n * (n + 1)) / 2

    num_sum = 0
    for num in nums:
        num_sum += num

    return n_sum - num_sum


assert find_missing_number_1([3, 0, 1]) == 2
assert find_missing_number_2([3, 0, 1]) == 2
assert find_missing_number_1([9, 6, 4, 2, 3, 5, 7, 0, 1]) == 8
assert find_missing_number_2([9, 6, 4, 2, 3, 5, 7, 0, 1]) == 8
assert find_missing_number_1([0]) == 1
assert find_missing_number_2([0]) == 1

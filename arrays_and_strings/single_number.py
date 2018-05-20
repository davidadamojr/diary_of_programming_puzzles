"""
Given a non-empty array of integers, every element appears twice except one.
Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it 
without using extra memory?
"""


def single_number(nums):
    frequency_map = {}
    for num in nums:
        frequency_map[num] = frequency_map.get(num, 0) + 1

    for num, frequency in frequency_map.items():
        if frequency == 1:
            return num

    return None

assert single_number([1, 5, 1, 2, 2, 6, 4, 5, 6]) == 4
assert single_number([1]) == 1
assert single_number([]) is None
print("All tests passed successfully.")

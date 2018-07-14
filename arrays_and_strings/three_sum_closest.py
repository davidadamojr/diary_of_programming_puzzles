"""
Given an array "nums" of n integers and an integer "target", find three integers in nums such that the sum is closest
to "target". Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example:
Given array nums = [-1, 2, 1, -4], and target = 1.
The sum that is closest to the target is 2. (-1 + 2 + 1 = 2)
"""


def three_sum_closest(nums, target):
    if not nums:
        return 0

    nums.sort()
    difference = float('inf')
    target_sum = 0
    for i in range(0, len(nums)-2):
        j = i + 1
        k = len(nums) - 1
        while j < k:
            first_num = nums[i]
            second_num = nums[j]
            third_num = nums[k]
            element_sum = first_num + second_num + third_num

            if element_sum < target:
                j += 1
            elif element_sum > target:
                k -= 1
            else:
                return element_sum

            current_difference = abs(element_sum - target)
            if current_difference < difference:
                difference = current_difference
                target_sum = element_sum

    return target_sum


assert three_sum_closest([-1, 2, 1, -4], 1) == 2
assert three_sum_closest([], 1) == 0
print("All tests passed successfully.")
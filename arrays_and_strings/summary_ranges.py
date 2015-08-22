"""
Given a sorted integer array without duplicates, return the summary of its
ranges.

For example, given [0,1,2,4,5,7], return ["0->2","4->5","7"].

Leetcode problem: https://leetcode.com/problems/summary-ranges/
"""

# @param {integer[]} nums list of sorted integer numbers
# @return {string[]} list of strings representing ranges
def summary_ranges(nums):
    if nums == []:
        return []
    
    ranges = []
    trailing_index = 0
    leading_index = 1
    while leading_index < len(nums):
        if nums[leading_index] - nums[leading_index-1] == 1:
            leading_index = leading_index + 1
        else:
            range_string = get_string(nums, trailing_index, leading_index-1)
            ranges.append(range_string)
            trailing_index = leading_index
            leading_index = leading_index + 1
        
    range_string = get_string(nums, trailing_index, leading_index-1)
    ranges.append(range_string)
    
    return ranges

# constructs a range string in the form "0->9"
def get_string(nums, start, end):
    if start == end:
        return str(nums[start])
    else:
        return str(nums[start]) + "->" + str(nums[end])

if __name__ == '__main__':
    numbers = [1,2,3,4,6,9,10,25,26,27,29]
    print summary_ranges(numbers)
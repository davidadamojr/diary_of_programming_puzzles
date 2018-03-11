"""
Given an array of integers, 1<=a[i]<=n (n = size of array), some elements appear twice and others appear once. Find
all elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?

https://leetcode.com/problems/find-all-duplicates-in-an-array/description/
"""


def find_duplicates(nums):
    duplicates = []
    already_found = {}

    for num in nums:
        already_found[num] = already_found.get(num, 0) + 1

    for num, times_found in already_found.items():
        if times_found > 1:
            duplicates.append(num)

    return duplicates


def find_duplicates_linear_time(nums):
    duplicates = []
    for num in nums:
        location = abs(num) - 1
        if nums[location] < 0:
            duplicates.append(abs(num))
        else:
            nums[location] = -nums[location]

    return duplicates



if __name__ == "__main__":
    assert find_duplicates([]) == []
    assert find_duplicates([1,2,3,4,5]) == []
    assert find_duplicates([1,4,2,3,5]) == []
    assert find_duplicates([1,3,4,2,3,6,7,4,5]) == [3, 4]
    assert find_duplicates([1,2,3,3,4,4,5,6,7]) == [3,4]

    assert find_duplicates_linear_time([]) == []
    assert find_duplicates_linear_time([1, 2, 3, 4, 5]) == []
    assert find_duplicates_linear_time([1, 4, 2, 3, 5]) == []
    assert find_duplicates_linear_time([1, 3, 4, 2, 3, 6, 7, 4, 5]) == [3, 4]
    assert find_duplicates_linear_time([1, 2, 3, 3, 4, 4, 5, 6, 7]) == [3, 4]
    print("All test cases passed successfully.")
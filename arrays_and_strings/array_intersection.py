"""
Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2, 2]

Note: 
- Each element in the result should appear as many times as it shows in both arrays
- The result can be in any order
"""


def find_intersection(first_num_lst, second_num_lst):
    num_hash = {}
    for num in first_num_lst:
        if num in num_hash:
            num_hash[num] = num_hash[num] + 1
        else:
            num_hash[num] = 1

    intersection_lst = []
    for num in second_num_lst:
        if num in num_hash and num_hash[num] > 0:
            intersection_lst.append(num)
            num_hash[num] = num_hash[num] - 1

    return intersection_lst


if __name__ == '__main__':
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    assert find_intersection(nums1, nums2) == [2, 2]

    nums1 = []
    nums2 = [2, 2]
    assert find_intersection(nums1, nums2) == []

    nums1 = [2, 2]
    nums2 = []
    assert find_intersection(nums1, nums2) == []

    nums1 = []
    nums2 = []
    assert find_intersection(nums1, nums2) == []

    print("All test cases passed.")

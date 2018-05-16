"""
Rotate an array of n elements to the right by k steps.

For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to 
[5,6,7,1,2,3,4]

Leetcode question: https://leetcode.com/problems/rotate-array/
"""


def rotate(nums, k):
    # nums is a list of integers
    # k is the number of steps by which to rotate
    # reverse 0..k-1, reverse k..n, then reverse 0..n
    n = len(nums)
    k = k % n  # it is possible for k > n

    def reverse(start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start = start + 1
            end = end - 1

    reverse(0, n - k - 1)
    reverse(n - k, n - 1)
    reverse(0, n - 1)

    return nums


if __name__ == '__main__':
    print(rotate([1, 2, 3, 4, 5, 6, 7], 3))
    print(rotate([1, 2, 3, 4], 5))

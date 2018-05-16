"""Given an array "nums", write a function to move all 0's to the end of it 
while maintaining the relative order of the non-zero elements.

For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums 
should be [1, 3, 12, 0, 0].

Note:
1. You must do this in-place without making a copy of the array
2. Minimize the total number of operations

https://leetcode.com/problems/move-zeroes/
"""


def move_zeros(num):
    trailing_idx = 0
    leading_idx = 1
    num_len = len(num)
    while leading_idx < num_len:
        if num[trailing_idx] == 0:
            if num[leading_idx] != 0:
                num[leading_idx], num[trailing_idx] = num[trailing_idx], num[leading_idx]
                trailing_idx = trailing_idx + 1
                leading_idx = leading_idx + 1
            else:
                leading_idx = leading_idx + 1
        else:
            trailing_idx = trailing_idx + 1
            leading_idx = leading_idx + 1

    return num


if __name__ == '__main__':
    assert move_zeros([0, 1, 0, 3, 12]) == [1, 3, 12, 0, 0]
    assert move_zeros([0, 0, 0, 0, 0]) == [0, 0, 0, 0, 0]
    print("All test cases passed")

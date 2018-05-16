"""
Given an index k, return the kth row of the Pascal's triangle.

For example, given k = 3, return [1,3,3,1]

Leetcode question: https://leetcode.com/problems/pascals-triangle-ii/
"""


def get_pascal_row(row_index):
    """Optimized for O(k) space"""
    row = [0 for i in range(0, row_index + 1)]

    for row_num in range(0, row_index + 1):
        for col_num in range(row_num, -1, -1):
            if col_num == row_num or col_num == 0:
                row[col_num] = 1
            else:
                row[col_num] = row[col_num - 1] + row[col_num]

    return row


if __name__ == '__main__':
    print(get_pascal_row(4))

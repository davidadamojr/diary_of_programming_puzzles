"""
A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same element. Now given an MxN matrix, 
return True if and only if the matrix is Toeplitz.

Example 1:
Input: matrix = [[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]]
Output: True
Explanation:
1234
5123
9512

In the above grid, the diagonals are "[9]", "[5, 5]', "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]"
Note:
1. matrix will be a 2D array of integers
2. matrix will have a number of rows and columns in range [1, 20]
3. matrix[i][j] will be integers in range [0, 99]

https://leetcode.com/problems/toeplitz-matrix/description/
"""


def is_toeplitz_matrix(matrix):
    for row_idx, row in enumerate(matrix):
        for col_idx, value in enumerate(row):
            if col_idx == 0 or row_idx == 0:
                continue

            if value != matrix[row_idx - 1][col_idx - 1]:
                return False

    return True

assert is_toeplitz_matrix([[1, 2, 3, 4],
                           [5, 1, 2, 3],
                           [9, 5, 1, 2]]) is True
assert is_toeplitz_matrix([[1, 2, 3, 4],
                           [5, 5, 5, 5],
                           [9, 9, 9, 9]]) is False
print("All tests passed successfully.")

"""
Given "numRows", generate the first "numRows" of Pascal's triangle.

For example, given numRows = 5, 

Return:
[
        [1],
       [1, 1],
     [1, 2, 1],
    [1, 3, 3, 1],
   [1, 4, 6, 4, 1]
]

Leetcode problem: https://leetcode.com/problems/pascals-triangle/
"""


# @param {integer} numRows
# @return {integer[][]}
def generate(numRows):
    pascals_triangle = []

    row = 0
    while row < numRows:
        if len(pascals_triangle) == 0:
            pascals_triangle.append([1])
        else:
            current_row = pascals_triangle[-1]
            new_row = [current_row[0]]
            for i in range(1, len(current_row)):
                new_row.append(current_row[i] + current_row[i - 1])
            new_row.append(1)
            pascals_triangle.append(new_row)

        row = row + 1

    return pascals_triangle


if __name__ == '__main__':
    print(generate(5))
    print(generate(10))

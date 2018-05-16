"""
Determine if a Sudoku is valid, according to http://sudoku.com.au/TheRules.aspx
The Sudoku board could be partially filled, where empty cells are filled with the 
character '.'

Note: A valid Sudoku board (partially filled) is not necessarily solvable. Only 
the filled cells need to be validated.

Leetcode problem: https://leetcode.com/problems/valid-sudoku/
"""


# @param board, a 9x9 2-dimensional list/array
# @return boolean indicating if the Sudoku board is valid
def is_valid_sudoku(board):
    row_hash = {}
    col_hash = {}
    grid_hash = {(i, j): set() for i in range(3) for j in range(3)}

    for i in range(9):
        for j in range(9):
            if board[i][j] in row_hash or board[j][i] in col_hash or board[i][j] in grid_hash[(i / 3, j / 3)]:
                return False
            else:
                if board[i][j] != '.':
                    row_hash[board[i][j]] = 1
                    grid_hash[(i / 3, j / 3)].add(board[i][j])

                if board[j][i] != '.':
                    col_hash[board[j][i]] = 1

        row_hash = {}
        col_hash = {}

    return True

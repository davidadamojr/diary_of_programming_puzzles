"""
Design an algorithm to figure out if someone has won a game of tic tac toe.
"""


class Piece:
    def __init__(self, empty):
        self.empty = empty

    def __str__(self):
        return self.type


# returns the winning piece - either a blue piece or a red piece
# returns an empty piece if there is no winner
# @param board is a dimensional array representing an nxn board
def has_won(board):
    # check if board is nxn
    if board == [] or len(board) != len(board[0]):
        return "Invalid board: please provide an nxn board."

    # check columns
    number_of_columns = len(board[0])
    last_row_index = len(board) - 1
    for i in range(0, number_of_columns):
        start_piece = board[0][i]
        if not start_piece.empty:
            for j in range(1, len(board)):
                current_piece = board[j][i]
                if start_piece != current_piece:
                    break
                elif start_piece == current_piece and j == last_row_index:
                    return start_piece

                    # check rows
    number_of_rows = len(board)
    last_column_index = len(board[0]) - 1
    for i in range(0, number_of_rows):
        start_piece = board[i][0]
        for j in range(1, number_of_columns):
            current_piece = board[i][j]
            if start_piece != current_piece:
                break
            elif start_piece == current_piece and j == last_column_index:
                return start_piece

    # check diagonals
    start_piece = board[0][0]
    last_index = number_of_rows - 1
    for i in range(1, number_of_rows):
        current_piece = board[i][i]
        if start_piece != current_piece:
            break
        elif start_piece == current_piece and i == last_index:
            return start_piece

    start_piece = board[last_index][0]
    row_index = last_index - 1
    column_index = 1
    while (row_index >= 0 and column_index < last_index):
        current_piece = board[row_index][column_index]
        if start_piece != current_piece:
            break
        elif start_piece == current_piece and row_index == 0:
            return start_piece
        row_index = row_index - 1
        column_index = column_index + 1

    return Piece(empty=True)


if __name__ == '__main__':
    blue_piece = Piece(False)
    blue_piece.type = "blue"
    red_piece = Piece(False)
    red_piece.type = "red"
    empty_piece = Piece(False)
    empty_piece.type = "empty"
    # 3x3 board
    board = [[empty_piece, blue_piece, blue_piece], [empty_piece, blue_piece, empty_piece],
             [blue_piece, blue_piece, red_piece]]

    print(has_won(board))

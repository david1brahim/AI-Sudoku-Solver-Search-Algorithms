class SudokuEnv:
    def __init__(self, board):
        self.board = board

    def is_valid(self, row, col, num):
        # Check row and column
        for i in range(9):
            if self.board[row][i] == num or self.board[i][col] == num:
                return False
        # Check 3x3 grid
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if self.board[start_row + i][start_col + j] == num:
                    return False
        return True

    def find_empty(self):
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == 0:
                    return i, j
        return None

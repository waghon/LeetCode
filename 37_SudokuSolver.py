class Solution:
    def solveSudoku(self, board):
        self.isSolved(board)

    def isSolved(self, board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    for num in range(10)[1:]:
                        if self.isValid(i, j, str(num), board):
                            board[i][j] = str(num)
                            if self.isSolved(board):
                                return True
                    board[i][j] = '.'
                    return False
        return True

    def isValid(self, pos_x, pos_y, num, board):
        for i in range(9):
            if board[pos_x][i] == num or board[i][pos_y] == num:
                return False
        subBox_x = int(pos_x / 3)
        subBox_y = int(pos_y / 3)
        for i in range(3):
            for j in range(3):
                if board[subBox_x * 3 + i][subBox_y * 3 + j] == num:
                    return False
        return True

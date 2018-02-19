import numpy as np

class Solution:
    def checkNineNums(self, nums):
        nums = np.array(nums)
        nums = nums.reshape(-1)
        isShown = [0 for i in range(10)]
        for s_num in nums:
            if s_num != '.':
                num = int(s_num)
                if isShown[num]:
                    return False
                else:
                    isShown[num] = 1
        return True

    def isValidSudoku(self, board):
        board = np.array(board)
        for row in board:
            if not self.checkNineNums(row):
                return False
        for i in range(9):
            column = board[:,i]
            if not self.checkNineNums(column):
                return False
        for i in range(3):
            for j in range(3):
                subBox = board[i*3:i*3+3,j*3:j*3+3]
                if not self.checkNineNums(subBox):
                    return False
        return True

'''
Solution 1:
    from the begin to the end. When encountering x*y, there are two choices (use it at least once or not).
    One is expand it to xx*y
    another is y

class Solution:
    def isMatch(self, s, p):
        if not p:
            return not s
        isFirstMatch = bool(s) and p[0] in {s[0], '.'}
        if len(p) > 1 and p[1] == '*':
            return ((isFirstMatch and self.isMatch(s[1:], p)) or 
                    self.isMatch(s, p[2:]))
        else:
            return isFirstMatch and self.isMatch(s[1:], p[1:])
'''

'''
Solution 2:
    try DP algorithm
'''
import numpy as np
class Solution:
    def isMatch(self, s, p):
        len_s = len(s)
        len_p = len(p)
        matchMatrix = np.zeros([len_s + 1, len_p + 1])
        matchMatrix[len_s][len_p] = 1
        for i in reversed(range(len_s + 1)):
            for j in reversed(range(len_p)):
                isFirstMatch = i < len_s and p[j] in {s[i], '.'}
                if j + 1 < len_p and p[j+1] == '*':
                    matchMatrix[i][j] = (isFirstMatch and matchMatrix[i+1][j]) or matchMatrix[i][j+2]
                else:
                    matchMatrix[i][j] = isFirstMatch and matchMatrix[i+1][j+1]
        return bool(matchMatrix[0][0])


while True:
    s = input()
    p = input()
    solution = Solution()
    print(solution.isMatch(s, p))

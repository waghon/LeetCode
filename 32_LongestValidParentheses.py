'''
Solution 1: use dp to solve, record the longest valid parentheses until the
index of i

Solution 2: use the stack to simulate the process of push of pop, during which
it can record how many numbers have been poped and pushed.
'''
class Solution:
    def longestValidParentheses(self, s):
        if len(s) < 1:
            return 0
        longestUntilNth = [0 for i in range(len(s))]
        for i in range(1, len(s)):
            if s[i] == ')':
                if s[i-1] == '(':
                    longestUntilNth[i] = 2
                    if i > 1:
                        longestUntilNth[i] += longestUntilNth[i-2]
                else:
                    toMatchPoint = i - 1- longestUntilNth[i-1]
                    if toMatchPoint >= 0 and s[toMatchPoint] == '(':
                        longestUntilNth[i] = 2 + longestUntilNth[i-1]
                        if toMatchPoint > 0:
                            longestUntilNth[i] += longestUntilNth[toMatchPoint-1]
        return max(longestUntilNth)

solution = Solution()
s = input()
print(solution.longestValidParentheses(s))

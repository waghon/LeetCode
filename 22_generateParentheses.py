class Solution:
    def generateParenRecursive(self, prefix, leftParen, rightParen, n):
        if len(prefix) == 2 * n:
            return [prefix]
        result = []
        if leftParen < n:
            result += self.generateParenRecursive(prefix+"(", leftParen + 1,
                                                      rightParen, n)
        if rightParen < leftParen:
            result += self.generateParenRecursive(prefix+")", leftParen,
                                                      rightParen + 1, n)
        return result

    def generateParentheses(self, n):
        return self.generateParenRecursive("", 0, 0, n)

solution = Solution()
n = int(input())
print(solution.generateParentheses(n))

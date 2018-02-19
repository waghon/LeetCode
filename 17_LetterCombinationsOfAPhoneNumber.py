'''
Solution 1: use iterations, save all the cambos before, then put the candidate
on it according to the next number
class Solution:
    def letterCombinations(self, digits):
        if len(digits) < 1:
            return []
        numberLetterDict = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs",
                            "tuv", "wxyz"]
        cambos = [""]
        for i in range(len(digits)):
            newCambos = []
            for cambo in cambos:
                for j in range(len(numberLetterDict[int(digits[i])])):
                    newCambos.append(cambo + numberLetterDict[int(digits[i])][j])
                    cambos = newCambos
        return cambos
'''

'''
Solution 2: try the recursive method
'''
class Solution:
    def letterCombinations(self, digits):
        numberLetterDict = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs",
                            "tuv", "wxyz"]
        if len(digits) < 1:
            return []
        if len(digits) == 1:
            result = []
            for i in range(len(numberLetterDict[int(digits[0])])):
                result.append(numberLetterDict[int(digits[0])][i])
            return result
        result = []
        nextPart = self.letterCombinations(digits[1:])
        for i in range(len(numberLetterDict[int(digits[0])])):
            for x in nextPart:
                result.append(numberLetterDict[int(digits[0])][i]+x)
        return result

solution = Solution()
digits = input()
print(solution.letterCombinations(digits))

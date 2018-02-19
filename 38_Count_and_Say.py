class Solution:
    def countAndSay(self, n):
        result = '1'
        while n > 1:
            result = self.getNextStr(result)
            n -= 1
        return result

    def getNextStr(self, strItem):
        result = ''
        count = 0
        for i in range(len(strItem)):
            count += 1
            if i == len(strItem) - 1 or strItem[i] != strItem[i+1]:
                result += str(count) + strItem[i]
                count = 0
        return result

solution = Solution()
n = int(input())
print(solution.countAndSay(n))

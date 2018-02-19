class Solution:
    def intToRoman(self, num):
        values = [ 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 ]
        numerals = [ "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V",
                    "IV", "I" ]
        resultStr = ""
        for i in range(len(values)):
            #print(keyWord)
            while num >= values[i]:
                resultStr += numerals[i]
                num -= values[i]
        return resultStr

solution = Solution()
while True:
    num = input()
    print(solution.intToRoman(int(num)))

'''
It is a good idea to split the integer into two parts. And them check if
partOne and partTwo will be the same or not.
Wrong Answer on case:
    1
    10
'''
class Solution:
    def isPalindrome(self, x):
        if x < 0:
            return False
        if x < 10:
            return True
        if x % 10 == 0:
            return False
        partOne = x
        partTwo = 0
        while(partOne > partTwo):
            partTwo = partTwo * 10 + partOne%10
            partOne = partOne // 10
        if partOne == partTwo or partTwo // 10 == partOne:
            return True
        else:
            return False

x = int(input())
solution = Solution()
print(solution.isPalindrome(x))


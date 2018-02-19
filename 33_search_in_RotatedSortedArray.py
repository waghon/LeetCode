# First try to use binary search to find the point
# The key of this problem is to judge which range to search
class Solution:
    def isInRange(self, start, end, target):
        if start <= target and target <= end:
            return True
        elif end < start and (target >= start or target <= end):
            return True
        else:
            return False

    def search(self, nums, target):
        if len(nums) == 0:
            return -1
        startIndex = 0
        endIndex = len(nums) - 1
        while startIndex <= endIndex:
            midIndex = int((startIndex + endIndex) / 2)
            if nums[midIndex] == target:
                return midIndex
            elif midIndex > startIndex and self.isInRange(nums[startIndex],
                                                 nums[midIndex - 1], target):
                endIndex = midIndex - 1
            elif midIndex < endIndex and self.isInRange(nums[midIndex+1],
                                                        nums[endIndex], target):
                startIndex = midIndex + 1
            else:
                return -1

solution = Solution()
nums = [int(x) for x in input().split()]
target = int(input())
print(solution.search(nums, target))

# Use binary search to find the left most and right
# most range

class Solution():
    def findLeftMost(self, nums, target):
        if len(nums) == 0:
            return -1
        begin = 0
        end = len(nums) -1
        while begin < end:
            mid = int((begin + end) / 2)
            if target <= nums[mid]:
                end = mid
            else:
                begin = mid + 1
        if nums[begin] == target:
            return begin
        else:
            return -1

    def findRightMost(self, nums, target):
        if len(nums) == 0:
            return -1
        begin = 0
        end = len(nums) -1
        while begin < end:
            mid = int((begin + end + 1) / 2)
            if target < nums[mid]:
                end = mid - 1
            else:
                begin = mid
        if nums[begin] == target:
            return begin
        else:
            return -1

    def searchRange(self, nums, target):
        leftMost = self.findLeftMost(nums, target)
        if leftMost == -1:
            return [-1, -1]
        else:
            return [leftMost, self.findRightMost(nums, target)]

solution = Solution()
nums = [int(x) for x in input().split()]
target = int(input())
print(solution.searchRange(nums, target))

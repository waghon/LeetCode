class Solution:
    def searchInsert(self, nums, target):
        if len(nums) == 0:
            return 0
        begin = 0
        end = len(nums) - 1
        while begin < end:
            mid = int((begin + end) / 2)
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                begin = mid + 1
            else:
                end = mid - 1
        if nums[begin] < target:
            return begin + 1
        else:
            return begin

solution = Solution()
nums = [int(x) for x in input().split()]
target = int(input())
print(solution.searchInsert(nums, target))

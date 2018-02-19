class Solution:
    def removeElement(self, nums, val):
        insertPosition = visitPosition = 0
        while visitPosition < len(nums):
            if nums[visitPosition] != val:
                nums[insertPosition] = nums[visitPosition]
                insertPosition += 1
            visitPosition += 1
        nums = nums[:insertPosition + 1]
        return insertPosition

solution = Solution()
nums = [int(x) for x in input().split()]
val = int(input())
print(solution.removeElement(nums, val))

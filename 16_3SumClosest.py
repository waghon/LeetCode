class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()
        #print(nums, target)
        closestNum = abs(target - (nums[0] + nums[1] + nums[2]))
        closestSum = nums[0] + nums[1] + nums[2]
        for i in range(len(nums) - 2):
            beginPoint = i + 1
            endPoint = len(nums) - 1
            while(beginPoint < endPoint):
                currentDiff = abs(target - nums[i] -
                                     nums[beginPoint] - nums[endPoint])
                if closestNum > currentDiff:
                    closestNum = currentDiff
                    closestSum = nums[i] + nums[beginPoint] + nums[endPoint]
                if nums[i] + nums[beginPoint] + nums[endPoint] > target:
                    endPoint -= 1
                elif nums[i] + nums[beginPoint] + nums[endPoint] == target:
                    return target
                else:
                    beginPoint += 1
        return closestSum



solution = Solution()
nums = [int(x) for x in input().split()]
target = int(input())
print(solution.threeSumClosest(nums,target))

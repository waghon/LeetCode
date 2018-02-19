class Solution:
    def fourSum(self, nums, target):
        #print(nums, target)
        nums.sort()
        result = []
        numsLength = len(nums)
        for i in range(numsLength - 3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, numsLength - 2):
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue
                beginPoint = j + 1
                endPoint = numsLength - 1
                remainSum = target - nums[i] - nums[j]
                while beginPoint < endPoint:
                    if (nums[beginPoint] + nums[endPoint] < remainSum):
                        beginPoint += 1
                    elif (nums[beginPoint] + nums[endPoint] > remainSum):
                        endPoint -= 1
                    else:
                        result.append([nums[i], nums[j], nums[beginPoint],
                                       nums[endPoint]])
                        while endPoint > beginPoint and nums[endPoint] == nums[endPoint-1]:
                            endPoint -= 1
                        while (beginPoint < endPoint and nums[beginPoint]
                               == nums[beginPoint+1]):
                            beginPoint += 1
                        beginPoint += 1
                        endPoint -= 1
        return result

solution = Solution()
nums = [int(x) for x in input().split()]
target = int(input())
print(solution.fourSum(nums, target))

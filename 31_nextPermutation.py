'''
Note:
    a[1:].sort is not working
    could use a[1:] = sorted(a[1:])
'''
class Solution:
    def nextPermutation(self, nums):
        numsLen = len(nums)
        stopPoint = None
        for i in range(numsLen - 1, -1, -1):
            if i == 0:
                nums.sort()
                return
            if nums[i] > nums[i-1]:
                stopPoint = i
                break
        toPermutatePart = nums[stopPoint-1:]
        for i in range(len(toPermutatePart)-1, -1, -1):
            if toPermutatePart[i] > toPermutatePart[0]:
                toPermutatePart[0], toPermutatePart[i] = (toPermutatePart[i],
                                                          toPermutatePart[0])
                break
        restPart = toPermutatePart[1:]
        restPart.sort()
        toPermutatePart[1:] = restPart
        nums[stopPoint-1:] = toPermutatePart

solution = Solution()
nums = [int(x) for x in input().split()]
solution.nextPermutation(nums)
print(nums)

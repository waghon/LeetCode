class Solution:
    def __init__(self):
        self.isSorted = False
    def combinationSum(self, candidates, target):
        if not self.isSorted:
            candidates.sort()
        if len(candidates) == 0:
            return []
        if target < candidates[0]:
            return []
        if target == candidates[0]:
            return [[candidates[0]]]
        useFirstPart = self.combinationSum(candidates, target - candidates[0])
        if len(useFirstPart) > 0:
            #print(useFirstPart)
            useFirstPart = [[candidates[0]]+x for x in useFirstPart]
        notUseFirstPart = self.combinationSum(candidates[1:], target)
        #print(notUseFirstPart)
        return useFirstPart + notUseFirstPart

solution = Solution()
candidates = [int(x) for x in input().split()]
target = int(input())
print(solution.combinationSum(candidates, target))

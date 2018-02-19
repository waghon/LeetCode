class Solution:
    def __init__(self):
        self.isSorted = False
    def combinationSum2(self, candidates, target):
        if not self.isSorted:
            candidates.sort()
        if len(candidates) == 0:
            return []
        if target < candidates[0]:
            return []
        if target == candidates[0]:
            return [[candidates[0]]]
        useFirstPart = self.combinationSum2(candidates[1:], target - candidates[0])
        if len(useFirstPart) > 0:
            #print(useFirstPart)
            useFirstPart = [[candidates[0]]+x for x in useFirstPart]
        nextCandidateIndex = 0
        while nextCandidateIndex < len(candidates) - 1:
            if candidates[nextCandidateIndex] != candidates[nextCandidateIndex+1]:
                break
            nextCandidateIndex += 1
        nextCandidateIndex += 1
        notUseFirstPart = self.combinationSum2(candidates[nextCandidateIndex:], target)
        #print(notUseFirstPart)
        return useFirstPart + notUseFirstPart

solution = Solution()
candidates = [int(x) for x in input().split()]
target = int(input())
print(solution.combinationSum(candidates, target))

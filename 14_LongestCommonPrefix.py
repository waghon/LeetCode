class Solution:
    def longestCommonPrefix(self, strs):
        #print(strs)
        if len(strs) < 1:
            return ""
        prefix = strs[0]
        for str in strs[1:]:
            while len(prefix) > 0:
                if str.find(prefix, 0, len(prefix)) != -1:
                    break
                prefix = prefix[:-1]
            if len(prefix) == 0:
                return ""
        return prefix

solution = Solution()
strs = [x for x in input().split()]
print(solution.longestCommonPrefix(strs))

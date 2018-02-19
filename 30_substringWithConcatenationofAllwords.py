class Solution:
    def findSubstring(self, s, words):
        #print(words)
        if len(s) == 0 or len(words) == 0:
            return []
        wordLen = len(words[0])
        numWords = len(words)
        sLen = len(s)
        windowSize = numWords * wordLen
        wordsDict = {}
        result = []
        for word in words:
            if word not in wordsDict:
                wordsDict[word] = 1
            else:
                wordsDict[word] += 1
        for startPoint in range(wordLen):
            windowBegin = startPoint
            if windowBegin + windowSize > sLen:
                continue
            windowDict = {}
            for key in wordsDict:
                windowDict[key] = 0
            numWordsInWindow = 0
            for i in range(numWords):
                word = s[windowBegin+i*wordLen : windowBegin+i*wordLen+wordLen]
                if word in wordsDict:
                    windowDict[word] += 1
                    if windowDict[word] <= wordsDict[word]:
                        numWordsInWindow += 1
            while True:
                if numWordsInWindow == numWords:
                    result.append(windowBegin)
                if windowBegin + windowSize + wordLen > sLen:
                    break
                outWord = s[windowBegin:windowBegin+wordLen]
                inWord = s[windowBegin+windowSize:windowBegin+windowSize+wordLen]
                if outWord in wordsDict:
                    windowDict[outWord] -= 1
                    if windowDict[outWord] < wordsDict[outWord]:
                        numWordsInWindow -= 1
                if inWord in wordsDict:
                    windowDict[inWord] += 1
                    if windowDict[inWord] <= wordsDict[inWord]:
                        numWordsInWindow += 1
                windowBegin += wordLen
        return result


solution = Solution()
s = input()
words = [x for x in input().split()]
print(solution.findSubstring(s, words))

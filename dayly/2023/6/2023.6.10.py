class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        queriesNum = self.f(queries)
        wordsNum = self.f(words).sort()
        n = len(wordsNum)
        res = []
        for i in queriesNum:
            left, right = 0, n - 1
            while left <= right:
                mid = (left + right) // 2
                if i > queriesNum[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
            res.append(n - left)
        return res

    def f(self, s: List[str]) -> List[int]:
        res = []
        for word in s:
            mi, num = ord(word[0]), 0
            for ele in word:
                if ord(ele) < mi:
                    mi = ord(ele)
                    num = 1
                if ord(ele) == mi:
                    num += 1
            res.append(num)
        return res


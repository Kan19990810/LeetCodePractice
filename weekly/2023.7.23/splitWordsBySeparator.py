class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        res = []
        for word in words:
            # print(word)
            ans = ''
            for i in word:
                # print(i)
                if i == separator:
                    if len(ans) != 0:
                        res.append(ans)
                    ans = ''
                else:
                    ans += i
            if len(ans) != 0:
                res.append(ans)
        return res

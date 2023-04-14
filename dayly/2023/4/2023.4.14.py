from collections import List


class Solution:


    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        n = len(queries)
        res = [True] * n
        for i in range(n):
            p = 0
            for c in queries[i]:
                if p < len(pattern) and pattern[p] == c:
                    p += 1
                elif c.isupper():
                    res[i] = False
                    break
            if p < len(pattern):
                res[i] = False
        return res


 - x
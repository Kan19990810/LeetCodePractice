from collections import Counter
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        res = []
        path = []
        n = len(tiles)
        s = Counter(tiles)

        def dfs(i):

            if i == n:
                if path not in res:
                    res.append(path.copy())
                return

            dfs(i + 1)

            for ele in s:
                if s[ele] != 0:
                    path.append(ele)
                    s[ele] -= 1
                    dfs(i + 1)
                    s[ele] += 1
                    path.pop()
        dfs(0)
        return len(res)


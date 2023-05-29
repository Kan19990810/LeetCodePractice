from math import inf
class Solution:
    # "eglglxa"
    # ["rs", "j", "h", "g", "fy", "l", "fc", "s", "zf", "i", "k", "x", "gl", "qr", "qj", "b", "m", "cm", "pe", "y", "ei",
    #  "wg", "e", "c", "ll", "u", "lb", "kc", "r", "gs", "p", "ga", "pq", "o", "wq", "mp", "ms", "vp", "kg", "cu"]
    # "leetscode"
    # ["leet", "code", "leetcode"]
    # "sayhelloworld"
    # ["hello", "world"]
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:


        @cache
        def dfs(s):
            ans = inf
            print(s)
            if all(i not in s for i in dictionary):
                return len(s)
            for i in dictionary:
                res = 0
                if i not in s:
                    continue
                a, b = len(s), len(i)
                for idx in range(a - b + 1):
                    if s[idx:idx + b] == i:
                        if s[:idx]:
                            res += dfs(s[:idx])
                        if s[idx + b:]:
                            res += dfs(s[idx + b:])
                ans = min(ans, res)
            return ans

        return dfs(s)

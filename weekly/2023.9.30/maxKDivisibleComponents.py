class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        ans = 1
        s = [False] * n

        g = [[] for _ in range(n)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)

        @cache
        def dfs(x):
            s[x] = True
            sum = values[x]
            for y in g[x]:
                if not s[y]:
                    t = dfs(s[y])
                    sum += t
                    if t % k == 0:
                        ans += 1

            return sum


        _ = dfs(0)

        return ans

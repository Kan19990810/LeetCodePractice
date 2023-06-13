class Solution:
    def getMoneyAmount(self, n: int) -> int:
        @cache
        def dfs(i, j):
            if i + 1 >= j:
                return j
            if i == j:
                return 0
            mid = (i + j) // 2
            return max(dfs(i, mid), dfs(mid, j)) + mid
        return dfs(1, n)
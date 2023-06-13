class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        n = len(values)
        dp = [[0] * n for _ in range(n)]
        for i in range(n - 3, -1, -1):
            for j in range(i + 2, n):
                res = inf
                for k in range(i + 1, j):
                    res = min(res, dp[i][k] + dp[k][j] + values[i] * values[k] * values[j])
                dp[i][j] = res
        return dp[0][n - 1]

        # @cache
        # def dfs(i, j):
        #     if i + 1 == j:
        #         return 0
        #     res = inf
        #     for c in range(i + 1, j):
        #         res = min(res, dfs(i, c) + dfs(c, j) + values[i] * values[c] * values[j])
        #     return res
        # return dfs(0, n - 1)
class Solution:
    def getMoneyAmount(self, n: int) -> int:

        dp = [[0] * n for _ in range(n)]

        for i in range(n - 1):
            dp[i][i + 1] = i + 1

        for i in range(n - 3, -1, -1):
            for j in range(i + 2, n):
                dp[i][j] = min(k + 1 + max(dp[i][k - 1], dp[k + 1][j]) for k in range(i + 1, j))

        return dp[0][n - 1]
        # @cache
        # def dfs(i, j):
        #     if i == j:
        #         return 0
        #     if i + 1 == j:
        #         return i
        #     return min(k + max(dfs(i, k - 1), dfs(k + 1, j)) for k in range(i + 1, j))
        # return dfs(1, n)

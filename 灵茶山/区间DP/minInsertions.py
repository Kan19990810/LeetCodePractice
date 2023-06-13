class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for i in range(n - 1):
            if s[i] != s[i + 1]:
                dp[i][i + 1] = 1
        for i in range(n - 3, -1, -1):
            for j in range(i + 2, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1]
                else:
                    dp[i][j] = min(dp[i + 1][j], dp[i][j - 1]) + 1
        return dp[0][n - 1]

        # @cache
        # def dfs(i, j):
        #     if i == j:
        #         return 0
        #     if i + 1 == j and s[i] == s[j]:
        #         return 0
        #
        #     if s[i] == s[j]:
        #         return dfs(i + 1, j - 1)
        #     else:
        #         return min(dfs(i + 1, j), dfs(i, j - 1)) + 1
        # return dfs(0, n - 1)
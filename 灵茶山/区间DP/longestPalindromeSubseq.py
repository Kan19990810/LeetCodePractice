class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)

        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1
        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])
        return dp[0][n - 1]
        
        # @cache
        # def dfs(i, j):
        #     if i == j:
        #         return 1
        #     if s[i] == s[j]:
        #         return dfs(i + 1, j - 1) + 2
        #     else:
        #         return max(dfs(i + 1, j), dfs(i, j - 1))
        # return dfs(0, n - 1)
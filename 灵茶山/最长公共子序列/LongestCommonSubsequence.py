from functools import cache
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n, m = len(text1), len(text2)

        # @cache
        # def dfs(a, b):
        #     if a < 0 or b < 0:
        #         return 0
        #     return dfs(a - 1, b - 1) + 1 if text1[a] == text2[b] else max(dfs(a - 1, b), dfs(a, b - 1))
        #
        # return dfs(n - 1, m - 1)

        # dp = [[0] * (m + 1) for _ in range(n + 1)]
        # for i in range(1, n + 1):
        #     for j in range(1, m + 1):
        #         dp[i][j] = dp[i - 1][j - 1] + 1 if text1[i - 1] == text2[j - 1] else max(dp[i - 1][j], dp[i][j - 1])
        # return dp[n][m]

        # dp = [[0] * (m + 1) for _ in range(2)]
        # for i in range(1, n + 1):
        #     for j in range(1, m + 1):
        #         dp[i % 2][j] = dp[(i - 1) % 2][j - 1] + 1 if text1[i - 1] == text2[j - 1] else max(dp[(i - 1) % 2][j], dp[i % 2][j - 1])
        # return dp[n % 2][m]

        dp = [0] * (m + 1)
        for i in range(1, n + 1):
            pre = dp[0]
            for j in range(1, m + 1):
                cmt = dp[j]
                dp[j] = pre + 1 if text1[i - 1] == text2[j - 1] else max(dp[j], dp[j - 1])
                pre = cmt
        return dp[m]

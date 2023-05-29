from functools import cache
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n, m = len(word1), len(word2)

        # @cache
        # def dfs(a, b):
        #     if a == 0:
        #         return b
        #     if b == 0:
        #         return a
        #     return dfs(a - 1, b - 1) if word1[a - 1] == word2[b - 1] else min(dfs(a, b - 1), dfs(a - 1, b)) + 1
        #
        # return dfs(n, m)

        # dp = [[0] * (m + 1) for _ in range(n + 1)]
        # for i in range(m + 1):
        #     dp[0][i] = i
        # for i in range(n + 1):
        #     dp[i][0] = i
        #
        # for i in range(1, n + 1):
        #     for j in range(1, m + 1):
        #         dp[i][j] = dp[i - 1][j - 1] if word1[i - 1] == word2[j - 1] else min(dp[i - 1][j], dp[i][j - 1]) + 1
        # return dp[n][m]

        # dp = [[0] * (m + 1) for _ in range(2)]
        # for i in range(m + 1):
        #     dp[0][i] = i
        #
        # for i in range(1, n + 1):
        #     dp[i % 2][0] = i
        #     for j in range(1, m + 1):
        #         dp[i % 2][j] = dp[(i - 1) % 2][j - 1] if word1[i - 1] == word2[j - 1] else min(dp[(i - 1) % 2][j], dp[i % 2][j - 1]) + 1
        # return dp[n % 2][m]

        dp = [0] * (m + 1)
        for i in range(m + 1):
            dp[i] = i

        for i in range(1, n + 1):
            pre = dp[0]
            dp[0] = i
            for j in range(1, m + 1):
                cmt = dp[j]
                dp[j] = pre if word1[i - 1] == word2[j - 1] else min(dp[j], dp[j - 1]) + 1
                pre = cmt
        return dp[m]

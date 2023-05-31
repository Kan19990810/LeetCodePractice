from functools import cache
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n, m = len(word1), len(word2)

        # @cache
        # def dfs(a, b):
        #     if a < 0:
        #         return b + 1
        #     if b < 0:
        #         return a + 1
        #     return dfs(a - 1, b - 1) if word1[a] == word2[b] else min(dfs(a, b - 1), dfs(a - 1, b),
        #                                                               dfs(a - 1, b - 1)) + 1
        #
        # return dfs(n - 1, m - 1)

        # dp = [[0] * (m + 1) for _ in range(n + 1)]
        # for i in range(m + 1):
        #     dp[0][i] = i
        # for i in range(n + 1):
        #     dp[i][0] = i
        #
        # for i in range(1, n + 1):
        #     for j in range(1, m + 1):
        #         dp[i][j] = dp[i - 1][j - 1] if word1[i - 1] == word2[j - 1] else min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
        #
        # return dp[n][m]

        # dp = [[0] * (m + 1) for _ in range(2)]
        # for i in range(m + 1):
        #     dp[0][i] = i
        #
        # for i in range(1, n + 1):
        #     dp[i % 2][0] = i
        #     for j in range(1, m + 1):
        #         dp[i % 2][j] = dp[(i - 1) % 2][j - 1] if word1[i - 1] == word2[j - 1] else min(dp[(i - 1) % 2][j], dp[i % 2][j - 1],
        #                                                                              dp[(i - 1) % 2][j - 1]) + 1
        #
        # return dp[n % 2][m]

        dp = [0] * (m + 1)
        for i in range(m + 1):
            dp[i] = i

        for i in range(1, n + 1):
            dp[0] = i
            pre = dp[0] - 1
            for j in range(1, m + 1):
                cmt = dp[j]
                dp[j] = pre if word1[i - 1] == word2[j - 1] else min(dp[j], dp[j - 1], pre) + 1
                pre = cmt

        return dp[m]

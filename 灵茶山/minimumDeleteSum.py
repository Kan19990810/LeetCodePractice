class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        n, m = len(s1), len(s2)

        # @cache
        # def dfs(a, b):
        #     if a < 0:
        #         s = 0
        #         for i in s2[:b + 1]:
        #             s += ord(i)
        #         return s
        #     if b < 0:
        #         s = 0
        #         for i in s1[:a + 1]:
        #             s += ord(i)
        #         return s
        #     return dfs(a - 1, b - 1) if s1[a] == s2[b] else min(dfs(a - 1, b) + ord(s1[a]), dfs(a, b - 1) + ord(s2[b]))
        # return dfs(n - 1, m - 1)

        # dp = [[0] * (m + 1) for _ in range(n + 1)]
        # for i in range(1, m + 1):
        #     dp[0][i] = dp[0][i - 1] + ord(s2[i - 1])
        # for i in range(1, n + 1):
        #     dp[i][0] = dp[i - 1][0] + ord(s1[i - 1])
        #
        # for i in range(1, n + 1):
        #     for j in range(1, m + 1):
        #         dp[i][j] = dp[i - 1][j - 1] if s1[i - 1] == s2[j - 1] else min(dp[i - 1][j] + ord(s1[i - 1]), dp[i][j - 1] + ord(s2[j - 1]))
        #
        # return dp[n][m]

        dp = [0] * (m + 1)
        for i in range(1, m + 1):
            dp[i] = dp[i - 1] + ord(s2[i - 1])

        for i in range(1, n + 1):
            pre = dp[0]
            dp[0] += ord(s1[i - 1])
            for j in range(1, m + 1):
                cmt = dp[j]
                dp[j] = pre if s1[i - 1] == s2[j - 1] else min(dp[j] + ord(s1[i - 1]), dp[j - 1] + ord(s2[j - 1]))
                pre = cmt

        return dp[m]

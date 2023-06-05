class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n, m, s= len(s1), len(s2), len(s3)
        if s != n +m:
            return False
        # dp = [[False] * (m + 1) for _ in range(n + 1)]
        # dp[0][0] = True
        # for i in range(m + 1):
        #     if s2[:i] == s3[:i]:
        #         dp[0][i] = True
        # for i in range(n + 1):
        #     if s1[:i] == s3[:i]:
        #         dp[i][0] = True
        #
        # for i in range(1, n + 1):
        #     for j in range(1, m + 1):
        #         if dp[i - 1][j]:
        #             dp[i][j] = True if s1[i - 1] == s3[i + j - 1] else False
        #         elif dp[i][j - 1]:
        #             dp[i][j] = True if s2[j - 1] == s3[i + j - 1] else False
        #         else:
        #             dp[i][j] = False
        # return dp[n][m]

        dp = [False] * (m + 1)
        dp[0] = True
        for i in range(m + 1):
            if s2[:i] == s3[:i]:
                dp[i] = True

        for i in range(1, n + 1):
            dp[0] = True if s1[:i] == s3[:i] else False
            for j in range(1, m + 1):
                if dp[j]:
                    dp[j] = True if s1[i - 1] == s3[i + j - 1] else False
                elif dp[j - 1]:
                    dp[j] = True if s2[j - 1] == s3[i + j - 1] else False
                else:
                    dp[j] = False
        return dp[m]


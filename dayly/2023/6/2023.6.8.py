import numpy as np
class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        n = len(reward1)
        diff = [0] * n
        for i in range(n):
            diff[i] = reward1[i] - reward2[i]

        diff = np.array(diff)
        reward1 = np.array(reward1)
        reward2 = np.array(reward2)
        arrIndex = np.array(diff).argsort()
        diff = diff[arrIndex]
        reward1 = reward1[arrIndex]
        reward2 = reward2[arrIndex]
        ans = 0
        for i in range(n):
            if i < k:
                ans += reward2[i]
            else:
                ans += reward1[i]

        return ans





        # dp = [[0] * (k + 1) for _ in range(n - k + 1)]
        # for i in range(1, k + 1):
        #     dp[0][i] = dp[0][i - 1] + reward1[i - 1]
        # for i in range(1, n - k + 1):
        #     dp[i][0] = dp[i - 1][0] + reward2[i - 1]
        # for i in range(1, n - k + 1):
        #     for j in range(1, k + 1):
        #         dp[i][j] = max(dp[i][j - 1] + reward1[i + j - 1], dp[i - 1][j] + reward2[i + j - 1])
        # return dp[n - k][k]
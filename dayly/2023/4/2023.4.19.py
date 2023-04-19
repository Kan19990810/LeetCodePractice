class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [0] * n
        for i in range(k):
            dp[i] = (i + 1) * max(arr[j] for j in range(i + 1))

        for i in range(k, n):
            for a in range(k):
                dp[i] = max(dp[i - k + a] + (k - a) * max(arr[j] for j in range(i - k + a + 1, i + 1)), dp[i])
        return dp[-1]

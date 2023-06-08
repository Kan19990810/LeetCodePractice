class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        pre_f0 = 0
        f0 = 0
        f1 = -inf
        for p in prices:
            new_f0 = max(f0, f1 + p)
            f1 = max(f1, pre_f0 - p)
            pre_f0 = f0
            f0 = new_f0
        return f0


        # dp = [[0] * 2 for _ in range(n + 1)]
        # dp[0][1] = -inf
        # for i, p in enumerate(prices):
        #     dp[i + 1][0] = max(dp[i][0], dp[i][1] + p)
        #     dp[i + 1][1] = max(dp[i][1], dp[i - 1][0] - p)
        # return dp[n][0]



        # @cache
        # def dfs(i, hold):
        #     if i < 0:
        #         return -inf if hold else 0
        #     if hold:
        #         return max(dfs(i - 1, True), dfs(i - 2, False) - prices[i])
        #     else:
        #         return max(dfs(i - 1, False), dfs(i - 1, True) + prices[i])
        # return dfs(n - 1, False)

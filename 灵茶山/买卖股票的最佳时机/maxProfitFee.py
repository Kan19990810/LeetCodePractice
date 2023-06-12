class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        f0, f1 = 0, -inf
        for i in prices:
            new_f0 = max(f0, f1 + i)
            f1 = max(f1, f0 - i - fee)
            f0 = new_f0
        return f0

        # dp = [[0] * 2 for _ in range(n + 1)]
        # dp[0][1] = -inf
        # for i, price in enumerate(prices):
        #     dp[i + 1][0] = max(dp[i][0], dp[i][1] + price)
        #     dp[i + 1][1] = max(dp[i][1], dp[i][0] - price - fee)
        # return dp[n][0] if dp[n][0] > 0 else 0

        # @cache
        # def dfs(i, hold):
        #     if i < 0:
        #         if hold:
        #             return -inf
        #         else:
        #             return 0
        #
        #     if hold:
        #         return max(dfs(i - 1, True), dfs(i - 1, False) - prices[i] - fee)
        #     else:
        #         return max(dfs(i - 1, False), dfs(i - 1, True) + prices[i] fee)
        #
        # ans = dfs(n - 1, False)
        # return ans if ans > 0 else 0

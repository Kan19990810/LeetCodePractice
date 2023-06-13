class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        f0, f1, f2 = 0, -inf, 0
        for i in prices:
            new_f1 = max(f1, f0 - i)
            f2 = max(f2, f1 + i)
            f1 = new_f1
        return f2 if f2 > 0 else 0
        
        # dp = [[0] * 3 for i in range(n + 1)]
        # dp[0][1] = -inf
        # for i, price in enumerate(prices):
        #     dp[i + 1][0] = dp[i][0]
        #     dp[i + 1][1] = max(dp[i][1], dp[i][0] - price)
        #     dp[i + 1][2] = max(dp[i][2], dp[i][1] + price)
        # return dp[n][2] if dp[n][2] > 0 else 0

        # @cache
        # def dfs(i, hold):
        #     if i < 0:
        #         if hold == 1:
        #             return -inf
        #         else:
        #             return 0
        #     if hold == 0:
        #         return max(dfs(i - 1, hold), dfs(i - 1, hold + 1) + prices[i])
        #     if hold == 1:
        #         return max(dfs(i - 1, hold), dfs(i - 1, hold + 1) - prices[i])
        #     if hold == 2:
        #         return dfs(i - 1, hold)
        # ans = dfs(n - 1, 0)
        # return ans if ans >= 0 else 0

        # mi, ma, ans = inf, 0, 0
        # for i in prices:
        #     if prices < mi:
        #         mi = prices
        #         ma = mi
        #     if prices > ma:
        #         ma = prices
        #         ans = max(ans, ma - mi)
        # return ans

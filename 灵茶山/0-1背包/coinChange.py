class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)

        # @cache
        # def dfs(i, c):
        #     if i < 0:
        #         return 0 if c == 0 else inf
        #     if c < coins[i]:
        #         return dfs(i - 1, c)
        #     return min(dfs(i - 1, c), dfs(i, c - coins[i]) + 1)
        #
        # ans = dfs(n - 1, amount)
        # return ans if ans < inf else -1

        # dp = [[inf] * (amount + 1) for _ in range(n + 1)]
        # dp[0][0] = 0
        # for i, x in enumerate(coins):
        #     for c in range(amount + 1):
        #         if c < x:
        #             dp[i + 1][c] = dp[i][c]
        #         else:
        #             dp[i + 1][c] = min(dp[i][c], dp[i + 1][c - x] + 1)
        # ans = dp[n][amount]
        # return ans if ans < inf else -1

        f = [inf] * (amount + 1)
        f[0] = 0
        for x in coins:
            for c in range(x, amount + 1):
                f[c] = min(f[c], f[c - x] + 1)
        ans = f[amount]
        return ans if ans < inf else -1

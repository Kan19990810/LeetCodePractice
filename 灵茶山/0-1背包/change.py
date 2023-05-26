class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        # @cache
        # def dfs(s, c):
        #     if s < 0:
        #         return 1 if c == 0 else 0
        #     if c < coins[s]:
        #         return dfs(s - 1, c)
        #     else:
        #         return dfs(s - 1, c) + dfs(s, c - coins[s])
        # ans = dfs(n - 1, amount)
        # return ans if ans > 0 else 0

        # dp = [[0] * (amount + 1) for _ in range(2)]
        # dp[0][0] = 1
        # for i, x in enumerate(coins):
        #     for c in range(amount + 1):
        #         if c < x:
        #             dp[(i + 1) % 2][c] = dp[i % 2][c]
        #         else:
        #             dp[(i + 1) % 2][c] = dp[i % 2][c] + dp[(i + 1) % 2][c - x]
        #
        # return dp[n % 2][amount]

        dp = [0] * (amount + 1)
        dp[0] = 1
        for x in coins:
            for c in range(x, amount + 1):
                dp[c] = dp[c] + dp[c - x]
        return dp[amount]
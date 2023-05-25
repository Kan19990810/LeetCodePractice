class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        # target = abs(target)
        target = target + sum(nums)
        if target % 2 != 0:
            return 0
        target //= 2
        #
        # def dfs(i, c):
        #     if i < 0:
        #         return 1 if c == 0 else 0
        #     if c < nums[i]:
        #         return dfs(i - 1, c)
        #     return dfs(i - 1, c) + dfs(i - 1, c - nums[i])
        #
        # return dfs(n - 1, target)

        # dp = [[0] * (abs(target) + 1) for _ in range(n + 1)]
        # dp[0][0] = 1
        #
        # for i, x in enumerate(nums):
        #     for c in range(target + 1):
        #         if c < x:
        #             dp[i + 1][c] = dp[i][c]
        #         else:
        #             dp[i + 1][c] = dp[i][c] + dp[i][c - x]
        # return dp[n][target]

        # dp = [[0] * (abs(target) + 1) for _ in range(2)]
        # dp[0][0] = 1
        #
        # for i, x in enumerate(nums):
        #     for c in range(target + 1):
        #         if c < x:
        #             dp[(i + 1) % 2][c] = dp[i % 2][c]
        #         else:
        #             dp[(i + 1) % 2][c] = dp[i % 2][c] + dp[i % 2][c - x]
        # return dp[n % 2][target]

        dp = [0] * (abs(target) + 1)
        dp[0] = 1
        for i, x in enumerate(nums):
            for c in range(target, x - 1, -1):
                dp[c] = dp[c] + dp[c - x]

        return dp[target]



class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)
        if target % 2 != 0:
            return False
        target //= 2
        n = len(nums)
        # @cache
        # def dfs(i, c):
        #     if i < 0:
        #         return True if c == 0 else False
        #     if c < nums[i]:
        #         return dfs(i - 1, c)
        #     return dfs(i - 1, c) or dfs(i - 1, c - nums[i])
        #
        # return dfs(n, target)

        dp = [[0] * (target + 1) for _ in range(n + 1)]
        dp[0][0] = True
        for i, x in enumerate(nums):
            for c in range(target + 1):
                if c < x:
                    dp[i + 1][c] = dp[i][c]
                dp[i + 1][c] = dp[i][c] or dp[i][c - nums[i]]
        return dp[n][target] == True

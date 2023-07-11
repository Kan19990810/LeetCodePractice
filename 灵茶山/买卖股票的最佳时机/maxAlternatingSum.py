class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        n = len(nums)
        f0, f1 = 0, -inf
        for i in nums:
            new_f0 = max(f0, f1 - i)
            f1 = max(f1, f0 + i)
            f0 = new_f0
        return f0

        # dp = [[0] * 2 for _ in range(n + 1)]
        # dp[0][1] = -inf
        # for i, num in enumerate(nums):
        #     dp[i + 1][0] = max(dp[i][0], dp[i][1] - num)
        #     dp[i + 1][1] = max(dp[i][1], dp[i][0] + num)
        # return dp[n][1]

        # @cache
        # def dfs(i, buff):
        #     if i < 0:
        #         if buff:
        #             return -inf
        #         else:
        #             return 0
        #
        #     if buff:
        #         return max(dfs(i - 1, True), dfs(i - 1, False) + nums[i])
        #     else:
        #         return max(dfs(i - 1, False), dfs(i - 1, True) - nums[i])
        #
        # return dfs(n - 1, True)

class Solution:
    def rob(self, nums: List[int]) -> int:
        # 动规规划

        n = len(nums)

        dp = [[0] * 2 for i in range(n)]

        dp[0][1] = nums[0]
        for i in range(1, n):
            # 第 i 家不偷
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1])

            # 第 i 家偷
            dp[i][1] = max(dp[i - 1][0], dp[i - 2][1]) + nums[i]

        return max(dp[n - 1][0], dp[n - 1][1])
    


        
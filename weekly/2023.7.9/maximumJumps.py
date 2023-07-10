class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        n = len(nums)
        # @cache
        # def dfs(idx, cum):
        #     if idx == n - 1:
        #         return cum
        #
        #     cur = cum
        #     for i in range(idx + 1, n):
        #         if abs(nums[i] - nums[idx]) <= target:
        #             cur = max(cur, dfs(i, cum + 1))
        #
        #     if cur == cum:
        #         return -1
        #     else:
        #         return cur
        #
        # return dfs(0, 0)

        # dp = [[0] * n for _ in range(n)]
        # # dp[i][j] 从 i 到 j 的最大跳跃次数
        # for i in range(1, n):
        #     if abs(nums[i] - nums[i - 1]) <= target:
        #         dp[i - 1][i] = 1
        #     else:
        #         dp[i - 1][i] = -1
        #
        # for i in range(n - 3, -1, -1):
        #     for j in range(i + 2, n):
        #         bo = False
        #         for k in range(i, j):
        #             if dp[i][k] == -1:
        #                 continue
        #             if abs(nums[j] - nums[k]) <= target:
        #                 dp[i][j] = max(dp[i][j], dp[i][k] + 1)
        #                 bo = True
        #         if not bo:
        #             dp[i][j] = -1
        # return dp[0][n - 1]

        dp = [0] * n

        for i in range(n - 2, -1, -1):
            bo = False
            for k in range(i + 1, n):
                if dp[k] == -1:
                    continue

                if abs(nums[i] - nums[k]) <= target:
                    dp[i] = max(dp[i], dp[k] + 1)
                    bo = True
                if not bo:
                    dp[i] = -1
        return dp[0] if dp[0] > 0 else -1

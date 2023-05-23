class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # n = len(nums)
        # target = target + sum(nums)
        # if target % 2 != 0:
        #     return 0
        # target //= 2
        #
        # def dfs(i, c):
        #     if i < 0:
        #         return 1 if c == 0 else 0
        #     if c < nums[i]:
        #         return dfs(i - 1, c)
        #     return dfs(i - 1, c) + dfs(i - 1, c - nums[i])
        #
        # return dfs(n - 1, target)


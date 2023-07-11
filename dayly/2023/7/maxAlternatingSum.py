from math import inf


class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        n = len(nums)

        @cache
        def dfs(i, buff):
            if i < 0:
                if buff:
                    return -inf
                else:
                    return 0

            if buff:
                return max(dfs(i - 1, True), dfs(i - 1, False) + nums[i])
            else:
                return max(dfs(i - 1, False), dfs(i - 1, True) - nums[i])

        return dfs(n - 1, True)

        # @cache
        # # i 以nums[i]为结尾的最大子序列交替和 k 0表示偶数标 1表示奇数标
        # def dfs(i, k):
        #     if i == 0:
        #         return nums[i] if k == 0 else -inf

        #     if k == 0:
        #         return max(nums[i], max(dfs(j, 1) + nums[i] for j in range(i))
        #     else:
        #         return max(dfs(j, 0) - nums[i] for j in range(i))

        # ans = max(dfs(i, 0) for i in range(n))
        # return ans

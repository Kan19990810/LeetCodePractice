class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        g = []
        for i in nums:
            left, right = 0, len(g) - 1
            while right >= left:
                mid = (left + right) // 2
                if i > g[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
            if left - 1 == len(g) - 1:
                g.append(i)
            else:
                g[left] = i
        return len(g)




        # dp = [0] * n
        #
        # for i in range(n):
        #     for j in range(i):
        #         if nums[i] > nums[j]:
        #             dp[i] = max(dp[i], dp[j])
        #     dp[i] += 1
        # return max(dp)



        # @cache
        # def dfs(n):
        #     res = 0
        #     for i in range(n):
        #         if nums[n] > nums[i]:
        #             res = max(res, dfs(i))
        #     return res + 1
        #
        # return max(dfs(i) for i in range(n))
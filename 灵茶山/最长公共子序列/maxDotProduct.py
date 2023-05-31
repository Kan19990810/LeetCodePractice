class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        n, m = len(nums1), len(nums2)

        # @cache
        # def dfs(a, b):
        #     if a == 0:
        #         return 0
        #     if b == 0:
        #         return 0
        #     if nums1[a - 1] * nums2[b - 1] > 0:
        #         return max(dfs(a - 1, b - 1) + nums1[a - 1] * nums2[b - 1], dfs(a - 1, b), dfs(a, b - 1))
        #     else:
        #         return max(dfs(a - 1, b), dfs(a, b - 1))
        # ans = dfs(n, m)
        # return ans if ans > 0 else max(max(nums1) * min(nums2), min(nums1) * max(nums2))

        # dp = [[0] * (m + 1) for _ in range(n + 1)]
        # for i in range(1, n + 1):
        #     for j in range(1, m + 1):
        #         dp[i][j] = max(dp[i - 1][j - 1] + nums1[i - 1] * nums2[j - 1], dp[i - 1][j], dp[i][j - 1])
        # ans = dp[n][m]
        # return ans if ans > 0 else max(max(nums1) * min(nums2), min(nums1) * max(nums2))

        dp = [0] * (m + 1)
        for i in range(1, n + 1):
            pre = 0
            for j in range(1, m + 1):
                cmt = dp[j]
                dp[j] = max(pre + nums1[i - 1] * nums2[j - 1], dp[j], dp[j - 1])
                pre = cmt
        ans = dp[m]
        return ans if ans > 0 else max(max(nums1) * min(nums2), min(nums1) * max(nums2))
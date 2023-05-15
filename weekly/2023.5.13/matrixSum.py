class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        n = len(nums)
        for i in range(n):
            nums[i].sort()

        m = len(nums[0])
        ans = 0
        ma = 0
        for i in range(m):
            ma = nums[0][i]
            for j in range(n):
                    ma = max(ma, nums[j][i])

            ans += ma

        return ans
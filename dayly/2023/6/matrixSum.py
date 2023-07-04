class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        n = len(nums)
        for i in range(n):
            nums[i].sort()
        m = len(nums[0])
        return sum(max(nums[i][j] for i in range(n)) for j in range(m))
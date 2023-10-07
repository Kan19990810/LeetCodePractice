class Solution:
    def minSizeSubarray(self, nums: List[int], target: int) -> int:
        dict = {}
        n = len(nums)
        
        p = [[0] * 2 * n for _ in range(2 * n)]

        for i in range(2 * n):
            p[i][i:] += nums[i % n]
        
        


class Solution:
    def minOperations(self, nums: List[int], target: int) -> int:
        n = len(nums)
        def dfs(i, k):
            if i == n - 1 and k == 0:
                return 
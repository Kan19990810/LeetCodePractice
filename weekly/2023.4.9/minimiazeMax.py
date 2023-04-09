class Solution:
    """
    动态规划
    下标 i 表示找 i 个下标对
    第 0 对 dp[0] = 0
    dp[i] 对 dp[i - 1]
    """
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums = sorted(nums)
        n = len(nums)
        for i in range(p):


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        pre = 0
        cur = 0
        for i in range(n):
            ma = max(pre + nums[i], cur)
            pre, cur = cur, ma
        return cur
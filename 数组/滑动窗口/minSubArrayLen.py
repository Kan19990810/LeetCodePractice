"""
给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的 连续 子数组，并返回其长度。如果不存在符合条件的子数组，返回 0。
"""
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float("inf")
        sum = 0
        i = 0
        for j in range(len(nums)):
            sum += nums[j]
            while sum >= target:
                res = min(res, j - i + 1)
                sum -= nums[i]
                i += 1
        if res == float("inf"):
            return 0
        else:
            return res
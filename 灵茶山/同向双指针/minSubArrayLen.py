class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        n = len(nums)
        an = n + 1
        s = left = 0
        for right, x in enumerate(nums):
            s += x
            while s - nums[left] >= target:
                s -= nums[left]
                left += 1
            if s >= target:
                an = min(an, right - left + 1)
        return an if an <= n else 0


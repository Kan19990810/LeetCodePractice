class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        ans = left = 0
        time =1
        for right, x in enumerate(nums):
            time *= x
            while time >= k:
                time /= nums[left]
                left += 1
            ans += right - left + 1
        return ans

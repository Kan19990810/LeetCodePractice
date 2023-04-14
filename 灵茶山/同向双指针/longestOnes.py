class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left, ans, count= 0, 0, 0

        for right, num in enumerate(nums):
            if num == 0:
                count += 1
                while count > k:
                    left += 1
                    count -= int(nums[left - 1] == 0)
            ans = max(ans, right - left + 1)
        return ans
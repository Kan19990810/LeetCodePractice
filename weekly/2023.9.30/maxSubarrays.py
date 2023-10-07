class Solution:
    def maxSubarrays(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return 1
        
        ans = 1
        left, right = 0, 1
        cur = nums[0]
        while right < n:
            if cur == 0:
                ans += 1
                left = right
                cur = nums[left]
            else:
                cur &= nums[right]
            right += 1
        if cur != 0 and ans > 1:
            ans -= 1

        return ans

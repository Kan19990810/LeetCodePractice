class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        nums1 = nums[:-1]
        nums2 = nums[1:]
        pre, cur = 0, 0
        for i in range(n - 1):
            pre, cur = cur, max(cur, pre + nums1[i])
        ans = cur
        pre, cur = 0, 0
        for i in range(n - 1):
            pre, cur = cur, max(cur, pre + nums2[i])
        ans = max(ans, cur)
        return ans

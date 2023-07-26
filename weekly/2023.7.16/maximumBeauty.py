class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        ans = 0
        num = 0
        first, second = 0, 0
        while second < n:
            if nums[second] - nums[first] < 2 * k:
                second += 1
                num += 1
                ans = max(ans, num)
            else:
                first += 1
                num -= 1
        return ans

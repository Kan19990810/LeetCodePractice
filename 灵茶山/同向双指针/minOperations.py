
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target, n= sum(nums) - x, len(nums)
        if target == 0:
            return n
        left, ans = 0, 0

        for right, num in enumerate(nums):
            target -= num

            while target < 0 and left < n:
                left += 1
                target += nums[left - 1]
                print(left, right, target)

            if target == 0:
                ans = max(ans, right - left + 1)

        return -1 if ans == 0 else n - ans


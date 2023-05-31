class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        nums.sort()
        ans = 1
        count, count0 = 0, 0
        n = len(nums)
        if n == 1:
            return nums[0]
        for x in nums:
            if x == 0:
                count0 += 1
                continue
            if x < 0:
                count += 1
            ans *= x

        if count % 2 != 0:
            ans //= nums[count - 1]
        if count == 1 and count0 + count == n:
            return 0

        return ans


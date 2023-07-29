class Solution:
    def maxArrayValue(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        if n == 1:
            return nums[0]

        first, second = n - 1, n - 2
        while second > -1:
            # print(first, second, nums[first], nums[second])
            if nums[first] >= nums[second]:
                nums[first] += nums[second]
                second -= 1
                ans = max(ans, nums[first])
            else:
                first = second
                ans = max(ans, nums[first])
                second -= 1
        return ans
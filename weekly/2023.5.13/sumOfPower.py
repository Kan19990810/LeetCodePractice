class Solution:
    def sumOfPower(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        nums.sort()

        pre = [0] * n
        pre[0] = nums[0]
        first, second = nums[0], 0
        for i in range(1, n):
            pre[i] = nums[i] + first
            second = pre[i] + first
            first = second
            # first += pre[i]

        for i in range(n):
            ans += (nums[i] ** 2) * pre[i]

        return ans % (10 ** 9 + 7)


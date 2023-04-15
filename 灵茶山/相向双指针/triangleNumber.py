class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        ans = 0
        for i in range(n - 1):

            for j in range(i + 1, n - 1):
                k = j + 1
                while k < n and nums[k] < nums[i] + nums[j]:
                    k += 1
                ans += k - j - 1
                print(i, j ,k)
        return ans

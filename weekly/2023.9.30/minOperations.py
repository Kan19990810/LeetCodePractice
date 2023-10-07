class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        s = set()
        n = len(nums)
        ans = 0
        for i in range(n - 1, -1, -1):
            ans += 1
            if nums[i] <= k and nums[i] not in s:
                s.add(nums[i])
                if len(s) == n:
                    return ans

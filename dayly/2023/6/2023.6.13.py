class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for a in range(n - 2):
            for b in range(a + 1, n - 1):
                if nums[a] == nums[b]:
                    continue
                for c in range(b + 1, n):
                    if nums[a] != nums[b] and nums[a] != nums[c] and nums[b] != nums[c]:
                        ans += 1
        return ans

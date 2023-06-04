class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        n = len(nums)
        first, last = 0, 0
        for idx, i in enumerate(nums):
            if i == 1:
                first = idx
            if i == n:
                last = idx
        if first < last:
            return first + n - last - 1
        else:
            return first + n - last - 2
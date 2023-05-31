class Solution:
    def averageValue(self, nums: List[int]) -> int:
        su, count = 0, 0
        for x in nums:
            if x % 3 == 0 and x % 2 == 0:
                su += x
                count += 1

        return su // count if count != 0 else 0
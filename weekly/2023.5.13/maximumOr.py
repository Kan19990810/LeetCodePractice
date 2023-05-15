class Solution:
    def maximumOr(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ma = nums[0]
        cur = 0

        for i in range(1, n):
            if len(bin(nums[i])) > len(bin(ma)):
                cur |= ma
                ma = nums[i]

            elif len(bin(nums[i])) == len(bin(ma)) and cur | ma | (nums[i] * (2 ** k)) > cur | nums[i] | (ma * (2 ** k)):
                cur |= ma
                ma = nums[i]

            else:
                cur |= nums[i]

        return cur | (ma * (2 ** k))


class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        neg, pos = 0, 0
        while nums[neg] > 0:
            neg += 1
        while nums[pos] < 0:
            pos += 1
        for i in range(n // 2):
            res[i * 2] = nums[pos]
            res[i * 2 + 1] = nums[neg]
            pos += 1
            neg += 1
            while neg < n and nums[neg] > 0:
                neg += 1
            while neg < n and nums[pos] < 0:
                pos += 1
        return res

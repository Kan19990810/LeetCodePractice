class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums
        res = []
        nums.sort()
        if nums[0] != nums[1] and nums[1] != nums[0] + 1:
            res.append(nums[0])
        for i in range(1, len(nums) - 1):
            if nums[i] != nums[i + 1] and nums[i + 1] != nums[i] + 1 and nums[i] != nums[i - 1] and nums[i - 1] != nums[i] - 1:
                res.append(nums[i])
        if nums[-1] != nums[-2] and nums[-1] != nums[-2] + 1:
            res.append(nums[-1])
        return res

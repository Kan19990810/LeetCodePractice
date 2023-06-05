class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0

        first = 0
        while first < n and nums[first] != 0:
            first += 1
        second = first
        while second < n:
            if nums[second] == 0:
                second += 1
            else:
                nums[first], nums[second] = nums[second], nums[first]
                first += 1
                second += 1
        return nums


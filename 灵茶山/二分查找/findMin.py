class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[-1] > nums[0]:
            return nums[0]

        left = 0
        right = len(nums) - 1

        while right >= left:

            if nums[right] >= nums[left]:
                return nums[left]

            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

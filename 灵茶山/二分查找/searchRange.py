class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def lower_bound(nums: List[int], target: int) -> int:
            left = 0
            right = len(nums)
            while left < right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid
            return left

        start = lower_bound(nums, target)
        if start == len(nums) or nums[start] != target:
            return [-1, -1]

        end = lower_bound(nums, target + 1) - 1
        return[start, end]
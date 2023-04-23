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

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def low_bound(nums: List[int], target: int) -> int:
            left = 0
            right = len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return right + 1

        start = low_bound(nums, target)
        end = low_bound(nums, target + 1) - 1
        if start == len(nums) or nums[start] != target:
            return [-1, -1]
        return [start, end]
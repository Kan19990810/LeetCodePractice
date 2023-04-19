class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = -1, len(nums) - 1  # 开区间 (-1, n-1)
        while left + 1 < right:  # 开区间不为空
            mid = (left + right) // 2
            if nums[mid] < nums[right]:  # 蓝色
                right = mid
            elif nums[mid] > nums[right]:  # 红色
                left = mid
            else:
                right -= 1
        return nums[right]


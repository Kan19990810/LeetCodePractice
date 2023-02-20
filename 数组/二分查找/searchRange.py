class Solution:
    def searchRange(self, nums: List[int], target: int) -> int:
        def getRightBorder(nums:List[int], target:int) -> int:
            left, right = 0, len(nums) - 1
            rightBorder = -2
            while left <= right:
                middle = left + (right - left) // 2
                if nums[middle] > target:
                    right =middle - 1
                else:
                    left = middle + 1
                    rightBorder = left
            return rightBorder

        def getleftBorder(nums:List[int], target:int) -> int :
            left, right = 0, len(nums) - 1
            leftBorder = -2
            while left <= right:
                middle = left + (right - left) // 2
                if nums[middle] >= target:
                    right = middle - 1
                    leftBorder = right
                else:
                    left = middle + 1
            return leftBorder

        leftBorder = getleftBorder(nums, target)
        rightBorder = getRightBorder(nums, target)

        if leftBorder == -2 or rightBorder == -2: return [-1, -1]

        if rightBorder - leftBorder > 1: return [leftBorder + 1,rightBorder - 1]

        return [-1, -1]

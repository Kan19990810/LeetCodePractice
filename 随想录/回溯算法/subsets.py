"""
给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

说明：解集不能包含重复的子集。

示例: 输入: nums = [1,2,3] 输出: [ [3],   [1],   [2],   [1,2,3],   [1,3],   [2,3],   [1,2],   []
"""
class Solution:
    def __init__(self):
        self.path: List[int] = []
        self.paths: List[List[int]] = []

    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.paths.clear()
        self.path.clear()
        self.backtracking(nums, 0)
        return self.paths
    def backtracking(self, nums: List[int], start_index: int) -> None:
        self.paths.append(self.path[:])
        if start_index == len(nums):
            return
        for i in range(start_index, len(nums)):
            self.path.append(nums[i])
            self.backtracking(nums, i + 1)
            self.path.pop()
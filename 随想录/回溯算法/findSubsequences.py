"""
给定一个整型数组, 你的任务是找到所有该数组的递增子序列，递增子序列的长度至少是2。

示例:

输入: [4, 6, 7, 7]
输出: [[4, 6], [4, 7], [4, 6, 7], [4, 6, 7, 7], [6, 7], [6, 7, 7], [7,7], [4,7,7]]
说明:

给定数组的长度不会超过15。
数组中的整数范围是 [-100,100]。
给定数组中可能包含重复数字，相等的数字应该被视为递增的一种情况
"""
class Solution:
    def __init__(self):
        self.paths = []
        self.path = []
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        self.backtracking(nums, 0)
        return self.paths

    def backtracking(self, nums: List[int], start_index: int):
        if len(self.path) >= 2:
            self.paths.append(self.path[:])
        if start_index == len(nums):
            return
        usage_list = [False] * 201
        for i in range(start_index, len(nums)):
            if(self.path and nums[i] < self.path[-1]) or usage_list[nums[i] + 100] == True:
                continue
            usage_list[nums[i] + 100] = True
            self.path.append(nums[i])
            self.backtracking(nums, i + 1)
            self.path.pop()
"""
给定一个 没有重复 数字的序列，返回其所有可能的全排列。

示例:

输入: [1,2,3]
输出: [ [1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1] ]
"""
class Solution:
    def __init__(self):
        self.path = []
        self.paths = []
    def permute(self, nums: List[int]) -> List[List[int]]:
        usage_list = [False] * len(nums)
        self.backtracking(nums, usage_list)
        return self.paths

    def backtracking(self, nums: List[int], usage_list: List[bool]) -> None:
        if len(self.path) == len(nums):
            self.paths.append(self.path[:])
            return

        for i in range(0, len(nums)):
            if usage_list[i] == True:
                continue
            usage_list[i] = True
            self.path.append(nums[i])
            self.backtracking(nums, usage_list)
            self.path.pop()
            usage_list[i] = False
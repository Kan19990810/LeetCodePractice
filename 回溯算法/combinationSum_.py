"""
给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的数字可以无限制重复被选取
"""
class Solution:
    def __init__(self):
        self.path = []
        self.paths = []
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.path.clear()
        self.path.clear()
        self.backtracking(candidates, target, 0, 0)
        return self.paths

    def backtracking(self, candidates: List[int], target: int, sum_: int, start_index: int) -> None:
        if sum_ == target:
            self.paths.append(self.path[:])
            return
        if sum_ > target:
            return
        for i in range(start_index, len(candidates)):
            sum_ += candidates[i]
            self.path.append(candidates[i])
            self.backtracking(candidates, target, sum_, i)
            sum_ -= candidates[i]
            self.path.pop()
"""
给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的每个数字在每个组合中只能使用一次。

说明： 所有数字（包括目标数）都是正整数。解集不能包含重复的组合
"""
class Solution:
    def __init__(self):
        self.paths = []
        self.path = []

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.paths.clear()
        self.path.clear()
        candidates.sort()
        self.backtracking(candidates, target, 0, 0)
        return self.paths

    def backtracking(self, candidates: List[int], target: int, sum_:int, start_index: int) -> None:
        if sum_ == target:
            self.paths.append(self.path[:])
            return
        for i in range(start_index, len(candidates)):
            if sum_ + candidates[i] > target:
                return
            if i > start_index and candidates[i] == candidates[i - 1]:
                continue
            sum_ += candidates[i]
            self.path.append(candidates[i])
            self.backtracking(candidates, target, sum_, i + 1)
            self.path.pop()
            sum_ -= candidates[i]

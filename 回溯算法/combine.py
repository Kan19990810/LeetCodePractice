"""
给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。

示例: 输入: n = 4, k = 2 输出: [ [2,4], [3,4], [2,3], [1,2], [1,3], [1,4], ]
"""
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        path = []
        def backtracking(n, k, startidx):
            if len(path) == k:
                result.append(path[:])
                return
            last_startidx = n - (k - len(path)) + 1

            for x in range(startidx, last_startidx + 1):
                path.append(x)
                backtracking(n, k, x + 1)
                path.pop()
        backtracking(n, k, 1)
        return result
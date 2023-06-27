class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        @cache  # 记忆化搜索
        def dfs(i: int, j: int) -> int:
            if i < 0: return -inf  # 子数组至少要有一个数，不合法
            if j == 0: return max(dfs(i - 1, 0), 0) + arr[i]
            return max(dfs(i - 1, 1) + arr[i], dfs(i - 1, 0))
        return max(max(dfs(i, 0), dfs(i, 1)) for i in range(len(arr)))




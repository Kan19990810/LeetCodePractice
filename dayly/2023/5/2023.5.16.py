class Solution:
    def minDifficulty(self, a: List[int], d: int) -> int:
        n = len(a)
        if n < d:
            return -1

        @cache  # 缓存装饰器，避免重复计算 dfs 的结果
        def dfs(i: int, j: int) -> int:
            if i == 0:  # 只有一天，必须完成所有工作
                return max(a[:j + 1])
            res, mx = inf, 0
            for k in range(j, i - 1, -1):
                mx = max(mx, a[k])  # 从 a[k] 到 a[j] 的最大值
                res = min(res, dfs(i - 1, k - 1) + mx)
            return res

        return dfs(d - 1, n - 1)

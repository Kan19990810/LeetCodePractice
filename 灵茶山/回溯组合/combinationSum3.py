class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []
        path = []

        def dfs(i, t):
            d = k - len(path)

            if t < 0 or t > (i + i - d + 1) * d // 2:
                return

            if d == 0 and t == 0:
                result.append(path.copy())
                return

            for j in range(i, d - 1, -1):
                path.append(j)
                dfs(j - 1, t - j)
                path.pop()

        return result
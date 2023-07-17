class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        ans = 0
        n, m = len(matrix), len(matrix[0])

        @cache
        def dfs(i, j):
            if i == -1:
                return 0
            if j == -1 or j == m:
                return inf

            return (
                min(dfs(i - 1, j - 1), dfs(i - 1, j), dfs(i - 1, j + 1)) + matrix[i][j]
            )

        ans = min(dfs(n - 1, j) for j in range(m))
        return ans

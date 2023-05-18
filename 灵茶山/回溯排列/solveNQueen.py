class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        path = [0] * n
        col = [False] * n
        diag1 = [False] * (2 * n - 1)
        diag2 = [False] * (2 * n - 1)
        def dfs(r):
            if r == n:
                res.append(['.' * c + 'Q' + '.' * (n - 1 - c) for c in path])
                return

            for c in range(n):
                if not col[c] and not diag1[r + c] and not diag2[r - c]:
                    col[c] = diag1[r + c] = diag2[r - c] = True
                    path[r] = c
                    dfs(r + 1)
                    col[c] = diag1[r + c] = diag2[r - c] = False
        dfs(0)
        return res

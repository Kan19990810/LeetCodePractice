class Solution:
    def differenceOfDistinctValues(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        ans = [[0] * n for _ in range(m)]
        if n <= m:
            for i in range(n):
                s = [grid[j][j + i] for j in range(n - i)]
                for j in range(n - i):
                    left = s[:j]
                    right = s[j + 1:]
                    ans[j][j + i] = abs(len(set(left)) - len(set(right)))

            for i in range(m - n):
                s = [grid[j + i][j] for j in range(n)]
                for j in range(n):
                    left = s[:j]
                    right = s[j + 1:]
                    ans[j + i][j] = abs(len(set(left)) - len(set(right)))

            for i in range(m - n, m):
                s = [grid[j + i][j] for j in range(m - i)]
                print(s)
                for j in range(n, m):
                    left = s[:j]
                    right = s[j + 1:]
                    ans[j + i][j] = abs(len(set(left)) - len(set(right)))

        else:
            for i in range(m):
                s = [grid[j + i][j] for j in range(m - i)]
                for j in range(m - i):
                    left = s[:j]
                    right = s[j + 1:]
                    ans[j + i][j] = abs(len(set(left)) - len(set(right)))

            for i in range(n - m):
                s = [grid[j][j + i] for j in range(m)]
                for j in range(m):
                    left = s[:j]
                    right = s[j + 1:]
                    ans[j][j + i] = abs(len(set(left)) - len(set(right)))

            for i in range(n - m, n):
                s = [grid[j][j + i] for j in range(m, n)]
                for j in range(m, n):
                    left = s[:j]
                    right = s[j + 1:]
                    ans[j][j + i] = abs(len(set(left)) - len(set(right)))

        return ans




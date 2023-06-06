class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        res, n = 0, len(grid)
        cnt = Counter(tuple(row) for row in grid)
        res = 0
        for j in range(n):
            res += cnt[tuple([grid[i][j] for i in range(n)])]
        return res
    #     for row in range(n):
    #         for col in range(n):
    #             if self.equal(row, col, n, grid):
    #                 res += 1
    #     return res
    #
    # def equal(self, row: int, col:int, n: int, grid: List[List[int]]) -> bool:
    #     for i in range(n):
    #         if grid[row][i] != grid[i][col]:
    #             return False
    #     return True
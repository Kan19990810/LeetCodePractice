class Solution:
    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        step = [[1, 2], [-1, 2], [2, 1], [2, -1], [1, -2], [-1, -2], [-2, 1], [-2, -1]]

        n = len(grid)
        total_n = n * n
        x,y = 0 ,0 
        if grid[x][y] != 0:
            return False

        for i in range(1, total_n):
            bo = False
            for xi, yi in  step:
                if 0 <= x + xi < n and 0 <= y + yi < n and grid[x + xi][y + yi] == i:
                    x += xi
                    y += yi
                    bo = True

            if bo == False: return False

        return True

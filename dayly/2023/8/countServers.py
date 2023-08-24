from collections import Counter
class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        cum = 0
        x_exist = Counter()
        y_exist = Counter()
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    cum += 1
                    x_exist[i] += 1
                    y_exist[j] += 1


        for i in range(n):
            if i in x_exist and x_exist[i] == 1:
                for j in range(m):
                    if grid[i][j] == 1 and j in y_exist and y_exist[j] == 1:
                        cum -= 1
        
        return cum

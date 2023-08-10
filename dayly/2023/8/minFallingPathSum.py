class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        # 递归 dfs (i, j, k) i 为 行， J 为列， 
        n = len(grid)
        # 记忆化搜索
        # @cache
        # def dfs(i, j, k):
        #     if i == n - 1:
        #         return k + grid[i][j]
            
        #     mn = inf
        #     for s in range(j):
        #         if dfs(i + 1, s, k + grid[i][j]) < mn:
        #             mn = dfs(i + 1, s, k + grid[i][j])
            
        #     for s in range(j+ 1, n):
        #         if dfs(i + 1, s, k + grid[i][j]) < mn:
        #             mn = dfs(i + 1, s, k + grid[i][j])
            
        #     return mn
        
        # return min(dfs(0, j, 0) for j in range(n)) 

        # 动规
        # dp = [[inf] * n for _ in range(n)]

        # for i in range(n):
        #     dp[0][i] = grid[0][i]

        # for i in range(1, n):
        #     for j in range(n):
        #         for k in range(j):
        #             dp[i][j] = min(dp[i][j], dp[i - 1][k])
        #         for k in range(j + 1, n):
        #             dp[i][j] = min(dp[i][j], dp[i - 1][k])
        #         dp[i][j] += grid[i][j]
        
        # res = min(dp[n - 1][j] for j in range(n))
        # return res
    
        # 转移过程优化
        first_min_sum, second_min_sum = 0, 0
        first_min_idx = -1
        for i in range(n):
            cur_first_min_sum, cur_second_min_sum = 10 ** 9, 10 ** 9
            cur_first_min_idx = -1
            for j in range(n):
                cur_sum = grid[i][j]
                if j != first_min_idx:
                    cur_sum += first_min_sum
                else:
                    cur_sum += second_min_sum
                if cur_sum < cur_first_min_sum:
                    cur_second_min_sum, cur_first_min_sum = cur_first_min_sum, cur_sum
                    cur_first_min_idx = j
                elif cur_sum < cur_second_min_sum:
                    cur_second_min_sum = cur_sum
            first_min_sum, second_min_sum = cur_first_min_sum, cur_second_min_sum
            first_min_idx = cur_first_min_idx
        return first_min_sum

from functools import cache
class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        # # 回溯枚举
        # 确定边界
        # r, c = len(grid), len(grid[0])
        # si, sj, n = 0, 0, 0
        # # 计数需要走过的格子数以及开始节点
        # for i in range(r):
        #     for j in range(c):
        #         if grid[i][j] == 0:
        #             n += 1
        #         elif grid[i][j] == 1:
        #             n += 1
        #             si, sj = i, j

        # #开始回溯
        # def dfs(i: int, j: int, n: int):
        #     # 到达终点， 走过所有格子返回1 条路径， 否则返回0条路径
        #     if grid[i][j] == 2:
        #         if n == 0:
        #             return 1 
        #         else:
        #             return 0
            
        #     # 记录当前格子状态，准备回溯状态
        #     t = grid[i][j]
        #     # 标记当前已经走过
        #     grid[i][j] = -1 
        #     # res 重置， 防止重复计数
        #     res = 0
        #     # 依次枚举上下左右
        #     for di, dj in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
        #         ni, nj = i + di, j + dj
        #         if 0 <= ni < r and 0 <= nj < c and grid[ni][nj] != -1:
        #             res += dfs(ni, nj, n -1)
        #     # 回溯当前格子状态        
        #     grid[i][j] = t
        #     return res
        # return dfs(si, sj, n)
            
        
        # 记忆化搜索+ 状态压缩 level up !!
        # grid 状态重复计算 使用记忆化搜索
        # 二进制表示未经过的点

        r, c = len(grid), len(grid[0])
        si, sj, st = 0, 0, 0
        for i in range(r):
            for j in range(c):
                # 将需要经过的格子 标注为 1
                if grid[i][j] in [0, 2]:
                    st |= (1 << (i * c + j))
                elif grid[i][j] == 1:
                    si, sj = i, j

        @cache
        def dp(i: int, j: int, st: int) -> int:
            if grid[i][j] == 2:
                # 只有当st 为0 时表示经过所有格子
                if st == 0:
                    return 1
                return 0
            res = 0
            for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                ni, nj = i + di, j + dj
                # st & (1 << (ni * c + nj)) 表示需要经过的格子可以经过
                if 0 <= ni < r and 0 <= nj < c and (st & (1 << (ni * c + nj))) > 0:
                    # 将经过的格子标注为 0
                    # 由于是形参传递 不需要恢复状态， 回溯为全局变量 需要恢复状态
                    res += dp(ni, nj, st ^ (1 << (ni * c + nj)))
            return res
        return dp(si, sj, st)
            
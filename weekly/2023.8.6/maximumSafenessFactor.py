class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        # # 最差的安全系数 为0
        # # 最大的距离为 inf
        # # 超出时间显示， 怎么剪枝
        # self.ans = 0
        # self.d = inf
        # n = len(grid)
        # # 找到所有小偷的单元格
        # thieves = []
        # for i in range(n):
        #     for j in range(n):
        #         if grid[i][j] == 1:
        #             thieves.append([i, j])

        # # 回溯
        # # 感觉递归不太好写
        # def dfs(i, j):
        #     # 到达终点 比较当前未知的安全系数和答案 返回最大安全系数
        #     # d为当前位置的安全系数
        #     if i == n - 1 and j == n - 1:
        #         self.ans = max(self.ans, self.d)
        #         return 
        #     res_d = 0
        #     # 记录当前位置的安全系数
        #     cmt = self.d
        #     for di, dj in [[0, 1], [1, 0]]:
        #         # 下一步要走的坐标
        #         ni, nj = i + di, j + dj
        #         # 计算下一步的安全系数
        #         if 0 <= ni <= n - 1 and 0 <= nj <= n - 1:
        #             for thief in thieves:
        #                 self.d = min(self.d, abs(ni - thief[0]) + abs(nj - thief[1]))
        #             dfs(ni, nj)

        #         # 恢复
        #         self.d = cmt

        # for thief in thieves:
        #     self.d = min(self.d, abs(0 - thief[0]) + abs(0 - thief[1]))
        # dfs(0, 0)
        # return self.ans
    

        n = len(grid)
        # 找到所有小偷的单元格
        thieves = []
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    thieves.append([i, j])

        # 用递归写的话用CACHE 减少时间复杂度， 或者动规划
        @cache
        def dfs(i, j, d):
            # 计算当前位置 的最小距离
            # cur_d = inf
            # for thief in thieves:
            #     cur_d = min(cur_d, abs(i - thief[0]) + abs(j - thief[1]))
            # res = max(cur_d, d)
            # # d 为到当前步 的最大安全距离
            if i == n - 1 and j == n - 1:
                return d
            res = d
            for di, dj in [[0, 1], [1, 0]]:
                # 下一步要走的坐标
                ni, nj = i + di, j + dj
                # 计算下一步的安全系数

                if 0 <= ni <= n - 1 and 0 <= nj <= n - 1:
                    # 下一步可行的时候
                    cur_d = inf
                    for thief in thieves:
                        cur_d = min(cur_d, abs(i - thief[0]) + abs(j - thief[1]))
                    res = max(res, dfs(ni, nj, cur_d))

            return res
        cur_d = inf
        for thief in thieves:
            cur_d = min(cur_d, abs(i - thief[0]) + abs(j - thief[1]))
        res = dfs(0, 0, cur_d)
        return res
            
    




            

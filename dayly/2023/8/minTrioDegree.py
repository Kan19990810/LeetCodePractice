from collection import defaultdict


class Solution:
    def minTrioDegree(self, n: int, edges: List[List[int]]) -> int:
        # g = [[0] * n for _ in range(n)]

        # degree = [0] * n

        # for x, y in edges:
        #     x, y = x - 1, y - 1
        #     g[x][y] = g[y][x] = 1
        #     degree[x] += 1
        #     degree[y] += 1

        # ans = inf

        # for i in range(n):
        #     for j in range(i + 1, n):
        #         if g[i][j] == 1:
        #             for k in range(j + 1, n):
        #                 if g[i][k] == g[j][k] == 1:
        #                     ans = min(ans, degree[i] + degree[j] + degree[k] - 6)

        # return -1 if ans == inf else ans

        # 构建有向图
        g = defaultdict(set)
        h = defaultdict(list)

        degree = [0] * n

        for x, y in edges:
            x, y = x- 1, y - 1
            g[x].add(y)
            g[y].add(x)
            degree[x] += 1
            degree[y] += 1

        for x, y in edges:
            x, y = x - 1, y - 1
            if degree[x] < degree[y] or (degree[x] == degree[y] and x < y):
                h[x].append(y)
            else:
                h[y].append(x)

        ans = inf
        for i in range(n):
            for j in h[i]:
                for k in h[j]:
                    if k in g[i]:
                        ans = min(ans, degree[i] + degree[j] + degree[k] - 6)
        
        return -1 if ans == inf else ans
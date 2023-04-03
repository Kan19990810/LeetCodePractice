"""
你有一个凸的 n 边形，其每个顶点都有一个整数值。给定一个整数数组 values ，其中 values[i] 是第 i 个顶点的值（即 顺时针顺序 ）。

假设将多边形 剖分 为 n - 2 个三角形。对于每个三角形，该三角形的值是顶点标记的乘积，三角剖分的分数是进行三角剖分后所有 n - 2 个三角形的值之和。

返回 多边形进行三角剖分后可以得到的最低分 。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/minimum-score-triangulation-of-polygon
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from math import inf
class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        n = len(values)
        dp = [[0] * n for _ in range(n)]
        for i in range(0, n - 2):
            dp[i][i + 2] = values[i] * values[i + 1] * values[i + 2]
            print(i, i+2, dp[i][i + 2])
        for i in range(n - 4, -1, -1):
            for j in range(i + 3, n):
                res = inf
                for k in range(i + 1, j):
                    res = min(res, dp[i][k] + dp[k][j] + values[i] * values[k] * values[j])
                dp[i][j] = res
                print(i, j, dp[i][j])
        return dp[0][-1]
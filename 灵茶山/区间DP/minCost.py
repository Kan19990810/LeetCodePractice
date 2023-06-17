class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts = [0] + sorted(cuts) + [n]
        m = len(cuts)

        dp = [[0] * m for _ in range(m)]

        for i in range(m - 3, - 1, -1):
            for j in range(i + 2, m):
                dp[i][j] = min(dp[i][k] +dp[k][j] for k in range(i + 1, j)) + cuts[j] - cuts[i]

        return dp[0][m - 1]


        # @cache
        # def dfs(i, j):
        #     if i + 1 == j:
        #         return 0
        #
        #     return min(dfs(i, k) + dfs(k, j) for k in range(i + 1, j)) + cuts[j] - cuts[i]
        #
        # return dfs(0, m - 1)
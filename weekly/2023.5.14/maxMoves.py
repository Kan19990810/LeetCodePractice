class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[0] * n] * m
        ans = 0

        if grid[0][1] > grid[0][0]:
            dp[0][1] = dp[0][0] + 1
        if grid[0][1] > grid[1][0]:
            dp[0][1] = max(dp[0][1], dp[1][0] + 1)
        ans = max(ans, dp[0][1])

        for j in range(1, m - 1):
            if grid[j][1] > grid[j - 1][0]:
                dp[j][1] = dp[j - 1][0] + 1
            if grid[j][1] > grid[j][0]:
                dp[j][1] = max(dp[j][1], dp[j][0] + 1)
            if grid[j][1] > grid[j + 1][0]:
                dp[j][1] = max(dp[j][1], dp[j + 1][0] + 1)
            ans = max(ans, dp[j][1])

        if grid[m - 1][1] > grid[m - 2][0]:
            dp[m - 1][1] = dp[m - 2][0] + 1
        if grid[m - 1][1] > grid[m - 1][0]:
            dp[m - 1][1] = max(dp[m - 1][1], dp[m - 1][0] + 1)
        ans = max(ans, dp[m - 1][1])

        for i in range(2, n):
            if grid[0][i] > grid[0][i - 1] and dp[0][i - 1] > 0:
                dp[0][i] = dp[0][i - 1] + 1
            if grid[0][i] > grid[1][i - 1] and dp[1][i - 1] > 0:
                dp[0][i] = max(dp[0][i], dp[1][i - 1] + 1)
            ans = max(ans, dp[0][i])

            for j in range(1, m - 1):
                if grid[j][i] > grid[j - 1][i - 1] and dp[j - 1][i - 1] > 0:
                    dp[j][i] = dp[j - 1][i - 1] + 1
                if grid[j][i] > grid[j][i - 1] and dp[j][i - 1] > 0:
                    dp[j][i] = max(dp[j][i], dp[j][i - 1] + 1)
                if grid[j][i] > grid[j + 1][i - 1] and dp[j + 1][i - 1] > 0:
                    dp[j][i] = max(dp[j][i], dp[j + 1][i - 1] + 1)
                ans = max(ans, dp[j][i])

            if grid[m - 1][i] > grid[m - 2][i - 1] and dp[m - 2][i - 1] > 0:
                dp[m - 1][i] = dp[m - 2][i - 1] + 1
            if grid[m - 1][i] > grid[m - 1][i - 1] and dp[m - 1][i - 1] > 0:
                dp[m - 1][i] = max(dp[m - 1][i], dp[m - 1][i - 1] + 1)
            ans = max(ans, dp[m - 1][i])
        return ans



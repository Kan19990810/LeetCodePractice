class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        m, n, mod = len(pizza), len(pizza[0]), 10 ** 9 + 7

        apples = [[0] * (n + 1) for _ in range(m + 1)]

        dp = [[[0 for j in range(n)] for i in range(m)] for _ in range(k + 1)]

        for i in range(m - 1, - 1, - 1):
            for j in range(n - 1, - 1, - 1):
                apples[i][j] = apples[i][j + 1] + apples[i + 1][j] - apples[i + 1][j + 1] + (pizza[i][j] == 'A')
                dp[1][i][j] = 1 if apples[i][j] > 0 else 0

        for k in range(1, k + 1):
            for i in range(m):
                for j in range(n):
                    for i2 in range(i + 1, m):
                        if apples[i][j] > apples[i2][j]:
                            dp[k][i][j] = (dp[k][i][j] + dp[k - 1][i2][j]) % mod
                    for j2 in range(j + 1, n):
                        if apples[i][j] > apples[i][j2]:
                            dp[k][i][j] = (dp[k][i][j] + dp[k - 1][i][j2]) % mod
        return dp[k][0][0]

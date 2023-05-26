import math
class Solution:
    def numSquares(self, n: int) -> int:
        # @cache
        #
        # def dfs(s, c):
        #     if s == 0:
        #         return 0 if c == 0 else inf
        #     if c < s ** 2:
        #         return dfs(s - 1, c)
        #     else:
        #         return min(dfs(s - 1, c), dfs(s, c - s ** 2) + 1)
        #
        # ans = dfs(int(math.sqrt(n)), n)
        #
        # return ans if ans < inf else -1

        # dp = [[inf] * (n + 1) for _ in range(2)]
        # dp[0][0] = 0
        # s = int(math.sqrt(n))
        # square = [i ** 2 for i in range(s + 1)]
        # for i in range(1, s + 1):
        #     for c in range(n + 1):
        #         if c < square[i]:
        #             dp[i % 2][c] = dp[(i - 1) % 2][c]
        #         else:
        #             dp[i % 2][c] = min(dp[(i - 1) % 2][c], dp[i % 2][c - square[i]] + 1)
        # ans = dp[s % 2][n]
        # return ans if ans < inf else -1

        dp = [inf] * (n + 1)
        dp[0] = 0
        s = int(math.sqrt(n))
        square = [i ** 2 for i in range(s + 1)]
        for i in range(s + 1):
            for c in range(square[i], n + 1):
                dp[c] = min(dp[c], dp[c - square[i]] + 1)
            print(dp)
        ans = dp[n]
        return ans if ans < inf else -1
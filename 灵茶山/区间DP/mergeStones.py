class Solution:
    def mergeStones(self, stones: List[int], k: int) -> int:
        n = len(stones)
        if (n - 1) % (k - 1) != 0:
            return -1
        d = [[[inf] * (k + 1) for _ in range(n)] for _ in range(n)]
        sum = [0] * n
        s = 0
        for i in range(n):
            d[i][i][1] = 0
            s += stones[i]
            sum[i] = s
        for L in range(2, n + 1):
            for l in range(n - L + 1):
                r = l + L - 1
                for t in range(2, k + 1):
                    for p in range(l, r , k - 1):
                        d[l][r][t] = min(d[l][r][t], d[l][p][1] + d[p + 1][r][t - 1])
                d[l][r][1] = min(d[l][r][1], d[l][r][k] + (sum[r] - (0 if l == 0 else sum[l - 1])))
        return d[0][n - 1][1]

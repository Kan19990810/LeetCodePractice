"""
有 N 堆石头排成一排，第 i 堆中有 stones[i] 块石头。

每次移动（move）需要将连续的 K 堆石头合并为一堆，而这个移动的成本为这 K 堆石头的总数。

找出把所有石头合并成一堆的最低成本。如果不可能，返回 -1 。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/minimum-cost-to-merge-stones
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
区间DP
"""
class Solution:
    def mergeStones(self, stones: List[int], k: int) -> int:
        n = len(stones)
        if (n - k) % (k - 1) != 0:
            return -1
        dp = [[0] * n for _ in range(0, n)]
        for i in range(n):
            dp[i][i] = stones[i]
        for i in range(n - k + 1, -1, -1):
            for j in range(i + k + 1, n, k - 1):
                dp[i][j] = min(dp[i + m][j - k + 1 + m] for m in range(k)) + sum(stones[m] for m in range(i, j + 1))
        return dp[0][-1]






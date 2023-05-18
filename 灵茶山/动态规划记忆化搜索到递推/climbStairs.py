class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        pre, cur = 1, 2
        for i in range(2, n):
            cur, pre = cur + pre, cur

        return cur
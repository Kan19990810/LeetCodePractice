class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        n = len(seats)
        pre, first = 0, 0
        ans = 0
        for i in range(n):
            if seats[i] == 1:
                if first == 0:
                    first = 1
                    pre = i
                    ans = pre
                else:
                    ans = max(ans, (i - pre) // 2)
                    pre = i
        ans = max(ans, n - 1 - pre)
        return ans

        
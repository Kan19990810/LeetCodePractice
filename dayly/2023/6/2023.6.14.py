class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        ma, ans = 0, 0
        for i, x in enumerate(flips):
            ma = max(ma, x)
            if i + 1 == ma:
                ans += 1
        return ans
class Solution:
    def minCount(self, coins: List[int]) -> int:
        res = 0
        for i in coins:
            res += (i + 1) // 2

        return res 
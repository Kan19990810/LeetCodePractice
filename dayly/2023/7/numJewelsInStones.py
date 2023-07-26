from collections import Counter
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        stone = Counter(stones)
        ans = 0
        for i in stone:
            if i in jewels:
                ans += stone[i]
        return ans
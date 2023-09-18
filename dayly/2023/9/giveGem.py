class Solution:
    def giveGem(self, gem: List[int], operations: List[List[int]]) -> int:
        for x, y in operations:
            t = gem[x] // 2
            gem[x] -= t
            gem[y] += t

        return max(gem) - min(gem)
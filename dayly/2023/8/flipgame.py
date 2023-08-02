class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        n = len(fronts)
        mn = inf
        invalid = set()
        for i in range(n):
            if fronts[i] == backs[i]:
                invalid.add(fronts[i])
        for i in range(n):
            if fronts[i] < mn and fronts[i] not in invalid:
                mn = fronts[i]
            if backs[i] < mn and backs[i] not in invalid:
                mn = backs[i]
        return mn if mn != inf else 0
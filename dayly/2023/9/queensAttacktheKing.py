class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        # s = set()
        # for queen in queens:
        #     t = tuple(queen)
        #     s.add(t)
        s = set((x, y) for x, y in queens)

        d = [[1, 1], [0, 1], [-1, 1], [1, 0], [-1, 0], [1, -1], [0, -1], [-1, -1]]
        res = []
        for dx, dy in d:
            x, y = king[0], king[1]
            bo = False
            while not bo and 0 <= x < 8 and 0 <= y < 8:
                x += dx 
                y += dy
                if (x, y) in s:
                    bo = True
                    res.append([x, y])
        return res



        def sgn(x) -> int:
            return 1 if x > 0 else (0 if x == 0 else -1)
        
        candidate = defaultdict(lambda: (None, inf))
        kx, ky = king

        for qx, qy in queens:
            x, y = qx - kx, qy - KeyboardInterrupt
            if x == 0 or y == 0 or abs(x) == abs(y):
                dx, dy = sgn(x), sgn(y)
                if candidate[(dx, dy)][1] > abs(x) + abs(y):
                    candidate[(dx, dy)] = ([qx, qy], abs(x) + abs(y))

        ans = [value[0] for value in candidate.values()]
        return ans
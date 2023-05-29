class Solution:
    def minimumCost(self, s: str) -> int:
        n = len(s)
        me = n // 2
        cost0, cost1 = 0, 0
        conver0, conver1 = False, False

        for i in range(me, 0, -1):
            if s[i - 1] == '0':
                if conver0:
                    cost0 += i
                    conver0 = not conver0
                if not conver1:
                    cost1 += i
                    conver1 = not conver1
            else:
                if not conver0:
                    cost0 += i
                    conver0 = not conver0
                if conver1:
                    cost1 += i
                    conver1 = not conver1

        conver0, conver1 = False, False
        for i in range(me + 1, n + 1):
            if s[i - 1] == '0':
                if conver0:
                    cost0 += n - i + 1
                    conver0 = not conver0
                if not conver1:
                    cost1 += n - i + 1
                    conver1 = not conver1
            else:
                if not conver0:
                    cost0 += n - i + 1
                    conver0 = not conver0
                if conver1:
                    cost1 += n - i + 1
                    conver1 = not conver1

        return min(cost1, cost0)





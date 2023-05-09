class Solution:
    def rampartDefensiveLine(self, rampart: List[List[int]]) -> int:


        def boolLine(rampart, num):
            n = len(rampart)
            for i in range(n - 2):
                m = num
                leavePre = n - (rampart[i + 1][0] - rampart[i][1])
                leaveNxt = rampart[i + 2][0] - rampart[i + 1][1] - leavePre
                if leavePre


        n = len(rampart)
        inter = [0] * (n - 1)
        for i in range(n - 1):
            inter[i] = rampart[i + 1][0] - rampart[i][1]

        left = inter[0]
        for _, element in enumerate(inter):
            left = min(element, left)

        right = sum(inter) // (n - 2)

        while right >= left:
            mi = (right + left) // 2








from collections import deque
from math import inf

class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        # 单调队列 deque 或者 heap
        
        n = len(points)
        pre, res = 0, -inf
        q = deque()
        q.append([points[0][0], points[0][1] - points[0][0]])
        for i in range(1, n):
            # print(q, i, points[i][1] + points[i][0])
            while len(q) > 0 and points[i][0] - q[0][0] > k:
                q.popleft()
            if len(q) > 0:
                res = max(res, points[i][1] + points[i][0] + q[0][1])    
            while len(q) > 0 and q[-1][1] < points[i][1] - points[i][0]:
                q.pop()
            q.append([points[i][0], points[i][1] - points[i][0]])

        return res
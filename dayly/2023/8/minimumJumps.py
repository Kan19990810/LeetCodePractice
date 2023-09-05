
from collections import deque
class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        # forbid = set(forbidden)

        # # 从x 跳回原点
        # def dfs(idx, back):
        #     if idx == 0:
        #         return 0
            
        #     if back == 1:
        #         if idx - a in forbid:
        #             return inf
        #         else:
        #             return 1 + dfs(idx - a, 0)
                
        #     else:
        #         if idx - a in forbid and idx + b in forbid:
        #             return inf
                
        #         if idx - a in forbid:
        #             return 1 + dfs(idx + b, 1)
                
        #         if idx + b in forbid:
        #             return 1 + dfs(idx - a, 0)
                
        #         return 1 + min(dfs(idx + b, 1), dfs(idx - a, 0))

        # ans = dfs(x, 0) 

        # return -1 if ans == inf else ans
        # 栈模拟广度优先算法 先进先出
        q, visited = deque([[0, 1, 0]]), set([0])
        # 限制范围
        lower, upper = 0, max(max(forbidden) + a, x) + b

        forbiddenSet = set(forbidden)
        # 对栈不为空的时候 表示可以往下走
        while q:
            # pop出下一步的操作
            position, direction, step = q.popleft()
            # 由于是广度优先，最先到达x位置的步数即为最佳步数
            if position == x:
                return step
            # 模拟往前走的情况
            nextPosition = position + a
            nextDirection = 1
            # 符合条件，则将往前走的步骤推入
            if lower <= nextPosition <= upper and nextPosition not in visited and nextPosition not in forbiddenSet:
                visited.add(nextPosition)
                q.append([nextPosition, nextDirection, step + 1])
            # 模拟往后的情况
            if direction == 1:
                nextPosition = position - b
                nextDirection = -1
                # 如果符合条件，则推入
                if lower <= nextPosition <= upper and nextPosition * nextDirection not in visited and nextPosition not in forbiddenSet:
                    visited.add(nextPosition * nextDirection)
                    q.append([nextPosition, nextDirection, step + 1])
        # 队列为空，则没有进一步走的情况
        return -1



class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # 并查集

        # pre = [-1] * numCourses


        # for requisites in prerequisites:
        #     pre[]

        # 
        # 记录直接关系
        g = [[] for _ in range(numCourses)]

        # 记录每个节点的入度
        indgree = [0] * numCourses

        # 记录是否有间接关系
        isPre = [[False] * numCourses for _ in range(numCourses)]
        for p in prerequisites:
            indgree[p[1]] += 1
            g[p[0]].append(p[1])

        # 队列入度为0的节点， 即为根节点
        q = []
        for i in range(numCourses):
            if indgree[i] == 0:
                q.append(i)

        while len(q) > 0:
            cur = q[0]
            q.pop(0)
            for ne in g[cur]:
                isPre[cur][ne] = True
                
                # 并查集关联根节点
                for i in range(numCourses):
                    isPre[i][ne] = isPre[i][ne] or  isPre[i][cur]
                
                # 操作子节点
                indgree[ne] -= 1

                # 子节点成为根节点
                if indgree[ne] == 0:
                    q.append(ne)

        res = []
        for query in queries:
            res.append(isPre[query[0]][query[1]])
        return res
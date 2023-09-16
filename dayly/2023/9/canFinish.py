class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 判断是否有环

        edges = collections.defaultdict(list)
        visited = [0] * numCourses

        result = list()
        valid = True

        # 构建一个图、树
        for info in prerequisites:
            edges[info[1]].append(info[0])

        # 深度优先遍历
        def dfs(i):
            nonlocal valid
            visited[i] = 1
            for j in edges[i]:
                if visited[j] == 0:
                    dfs(j)
                    if not valid:
                        return 
                elif visited[j] == 1:
                    valid = False
                    return 
            visited[i] = 2
            result.append(i)

        for i in range(numCourses):
            if valid and not visited[i]:
                dfs(i)

        return valid
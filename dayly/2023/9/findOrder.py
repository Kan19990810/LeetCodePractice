class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        edges = collections.defaultdict(list)
        visits = [0] * numCourses

        result = list()
        valid = True

        for requisite in prerequisites:
            edges[requisite[1]].append(requisite[0])

        def dfs(x):

            nonlocal valid
            visits[x] = 1

            for i in edges[x]:
                if visits[i] == 0:
                    dfs(i)
                    if not valid: return

                elif visits[i] == 1:
                    valid = False
                    return 
                
            visits[x] = 2
            result.append(x)
            return
        
        for i in range(numCourses):
            if valid and not visits[i]:
                dfs(i)

        return result[::-1] if valid else []

        

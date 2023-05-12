class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        path = []

        def dfs(i):

            d = k - len(path)

            if d == 0:
                result.append(path.copy())
                return

            for j in range(i, d - 1, -1):
                path.append(j)
                dfs(j - 1)
                path.pop()

        dfs(n)
        return result

class Solution:
    def queryString(self, s: str, n: int) -> bool:
        query = set()
        m = len(s)

        def dfs(i):
            if i == m:
                return

            for j in range(i, m):
                t = s[i: j + 1]
                if int(t, 2) not in query:
                    query.add(int(t, 2))

                dfs(j + 1)

        dfs(0)

        return True if all(i in query for i in range(1, n + 1)) else False

        
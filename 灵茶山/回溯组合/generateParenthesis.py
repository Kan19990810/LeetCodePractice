class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        m = n * 2
        result = []
        path = []

        def dfs(i, open):
            if i == m:
                result.append(''.join(path.copy()))

            if open < n:
                path.append('(')
                dfs(i + 1, open + 1)
                path.pop()

            if i - open < open:
                path.append(')')
                dfs(i + 1, open)
                path.pop()

        dfs(0, 0)
        return result


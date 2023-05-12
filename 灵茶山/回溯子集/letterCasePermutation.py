class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        n = len(s)
        ans = []
        path = []

        def dfs(i):
            if i == n:
                ans.append(path.copy())
                return

            path.append(s[i])
            dfs(i + 1)

            path.pop()
            if 'a' < s[i] < 'z':
                path.append(s[i].upper())
            else:
                path.append(s[i])

            dfs(i + 1)
            path.pop()

        dfs(0)
        return ans






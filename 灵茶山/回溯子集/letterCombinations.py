class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']

        ans = []
        path = [''] * n
        n = len(digits)

        if n == 0:
            return []

        def dfs(i):
            if i == n:
                ans.append(''.join(path))
                return

            for digit in mapping[int(digits[i])]:
                path[i] = digit
                dfs(i + 1)

        dfs(0)
        return ans

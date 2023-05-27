class Solution:
    def minLength(self, s: str) -> int:
        count = 0

        def dfs(idx, st):
            nonlocal count
            if idx >= len(st) - 1:
                return
            if st[idx] == 'A' and st[idx + 1] == 'B':
                count += 1
                if idx == 0:
                    dfs(idx, st[idx + 2:])
                else:
                    dfs(idx - 1, st[:idx] + st[idx + 2:])
            elif st[idx] == 'C' and st[idx + 1] == 'D':
                count += 1
                if idx == 0:
                    dfs(idx, st[idx + 2:])
                else:
                    dfs(idx - 1, st[:idx] + st[idx + 2:])
            else:
                dfs(idx + 1, st)
        dfs(0, s)
        return len(s) - 2 * count

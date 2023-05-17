class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        res = []
        lremove, rremove = 0, 0
        for i in s:
            if i == '(':
                lremove += 1
            elif i == ')':
                if lremove == 0:
                    rremove += 1
                else:
                    lremove -= 1

        def dfs(str, idx, lremove, rremove):
            if lremove == 0 and rremove == 0:
                cnt = 0
                for c in str:
                    if c == '(':
                        cnt += 1
                    elif c == ')':
                        cnt -= 1
                        if cnt < 0:
                            return
                if cnt == 0:
                    res.append(str)
                return

            for i in range(idx, len(str)):

                if i > idx and str[i] == str[i - 1]:
                    continue
                if lremove + rremove > len(str) - i:
                    break
                if lremove > 0 and s[i] == '(':
                    dfs(str[:i] + str[i + 1:], i, lremove - 1, rremove)
                if rremove > 0 and s[i] == ')':
                    dfs(str[:i] + str[i + 1:], i, lremove, rremove - 1)

        dfs(s, 0, lremove, rremove)
        return res

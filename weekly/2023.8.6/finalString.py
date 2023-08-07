class Solution:
    def finalString(self, s: str) -> str:
        n = len(s)
        res = ''
        for i in range(n):
            if s[i] == 'i':
                res = res[:: -1]
            else:
                res += s[i]
        return res

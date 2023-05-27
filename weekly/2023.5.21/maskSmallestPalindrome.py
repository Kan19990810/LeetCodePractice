class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        ans = list(s)
        cmt = s[::-1]
        n = len(s)
        for i in range(n // 2 + 1):
            if s[i] != cmt[i]:
                if s[i] <= cmt[i]:
                    ans[n - i - 1] = s[i]
                else:
                    ans[i] = cmt[i]
        return ''.join(ans)


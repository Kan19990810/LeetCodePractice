class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        n = len(s)
        first, second, third = 0, 1, 1
        ans = 1
        while third < n and s[third - 1] != s[third]:
            third += 1
        second = third
        if third >= n - 1:
            return n

        while third < n - 1:
            third += 1
            if s[third] == s[third - 1]:
                    ans = max(ans, third - first)
                    first = second
                    second = third


        ans = max(ans, third - first + 1)
        return ans
class Solution:
    def minimizedStringLength(self, s: str) -> int:
        ans = set()
        for i in s:
            if i not in ans:
                ans.add(i)
        return len(ans)

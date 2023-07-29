class Solution:
    def maxIncreasingGroups(self, usageLimits: List[int]) -> int:
        usageLimits.sort()
        ans = 1
        n = len(usageLimits)
        for i in range(1, n):
            if usageLimits[i] > usageLimits[i - 1]:
                ans += 1
            elif usageLimits[i] == usageLimits[i - 1]:
                if usageLimits[i] > ans:
                    ans += 1
        return ans
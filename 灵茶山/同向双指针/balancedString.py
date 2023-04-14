from collections import Counter
class Solution:
    def balancedString(self, s: str) -> int:
        count, m = Counter(s), len(s) // 4
        if all(count[i] == m for i in "QWER"):
            return 0
        ans, left = len(s), 0

        for right, letter in enumerate(s):
            count[letter] -= 1
            while all(count[i] <= m for i in "QWER"):
                left += 1
                count[s[left - 1]] += 1
                ans = min(ans, right - left + 2)
        return ans
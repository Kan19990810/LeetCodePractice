from collections import Counter
class Solution:


    def lengthOfLongestSubstring(self, s: str) -> int:
        ans, left = 0, 0
        dic = Counter()

        for right, letter in enumerate(s):
            dic[letter] += 1

            while dic[letter] > 1:
                dic[s[left]] -= 1
                left += 1

            ans = max(right - left + 1, ans)

        return ans
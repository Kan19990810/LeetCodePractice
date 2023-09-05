class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        ans = 0

        for i in range(low, high + 1):
            s = str(i)
            n = len(s)
            if sum(ord(s[j]) - ord('0') for j in range(n // 2)) == sum(ord(s[j]) - ord('0') for j in range(n // 2, n)):
                ans += 1

        return ans
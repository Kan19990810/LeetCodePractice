class Solution:
    def numberOfCuts(self, n: int) -> int:
        return n // 2 if n % 2 == 0 or n == 1 else n
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        s, c = 0, 1
        while n > 0:
            s += n % 10
            c *= n % 10
            n //= 10
        
        return c - s

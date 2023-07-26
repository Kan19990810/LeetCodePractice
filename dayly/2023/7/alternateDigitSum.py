class Solution:
    def alternateDigitSum(self, n: int) -> int:
        ans = 0
        bo = True
        while n > 0:
            re = n % 10
            n //= 10
            bo = not bo
            if bo:
                ans += re
            else:
                ans -= re
        return ans if bo else -ans

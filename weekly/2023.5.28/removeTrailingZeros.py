class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        num = num[::-1]
        i = 0
        while num[i] == '0':
            i += 1
        num = num[i:]
        return num[::-1]
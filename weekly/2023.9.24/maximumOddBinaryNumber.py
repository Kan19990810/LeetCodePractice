from collections import Counter
class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        items = Counter(s)
        res = ''
        for i in range(items['1'] - 1):
            res += '1'
        for i in range(items['0']):
            res += '0'
        res += '1'
        return res
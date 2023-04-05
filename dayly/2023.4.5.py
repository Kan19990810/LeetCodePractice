"""
给你两个正整数 a 和 b ，返回 a 和 b 的 公 因子的数目。

如果 x 可以同时整除 a 和 b ，则认为 x 是 a 和 b 的一个 公因子 。
"""
import math
class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        a, b = max(a, b), min(a, b)
        c = b
        while a % b != 0:
            c = a % b
            a = b
            b = c
        n, count = int(math.sqrt(c)), 0
        if c == n ** 2:
            for i in range(1, n):
                if c % i == 0:
                    count += 1
            return 2 * count + 1
        for i in range(1, n + 1):
            if c % i ==0:
                count += 1
        return 2 * count
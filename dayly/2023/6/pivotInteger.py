class Solution:
    def pivotInteger(self, n: int) -> int:
        l, r, a, b = 0, 0, 1, n
        while a < b:
            if l < r:
                l += a
                a += 1
            else:
                r += b
                b -= 1

        return a if l == r else -1

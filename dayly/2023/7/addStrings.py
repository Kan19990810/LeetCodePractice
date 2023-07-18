class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        n, m = len(num1), len(num2)
        if n < m:
            num1, num2 = num2, num1
            n, m = m, n

        num1 = num1[::-1]
        num2 = num2[::-1]
        num = ""
        add = 0
        for i in range(m):
            num += chr(ord("0") + ((add + int(num1[i]) + int(num2[i])) % 10))
            add = (add + int(num1[i]) + int(num2[i])) // 10

        for i in range(m, n):
            num += chr(ord("0") + ((add + int(num1[i])) % 10))
            add = (add + int(num1[i])) // 10

        if add == 1:
            num += "1"

        num = num[::-1]
        return num

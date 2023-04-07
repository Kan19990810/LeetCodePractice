"""
给你一个整数 n ，以二进制字符串的形式返回该整数的 负二进制（base -2）表示。

注意，除非字符串就是 "0"，否则返回的字符串中不能含有前导零。
"""
class Solution:
    def baseNeg2(self, n: int) -> str:
        if n == 0:
            return '0'
        neg = [[0] * 2 for _ in range(31)]
        num = [(-2) ** i for i in range(31)]
        neg[0] = [0, 1]
        neg[1] = [-2, 0]
        for i in range(2, 31):
            if i % 2 == 0:
                neg[i][0] = neg[i - 2][1]
                neg[i][1] = neg[i - 2][1] + (2 ** i)
            else:
                neg[i][0] = neg[i - 2][0] - (2 ** i)
                neg[i][1] = neg[i - 2][0]
        max_loc = 0
        while n > neg[max_loc][1]:
            max_loc += 2
        now_loc = max_loc
        now_num = n - num[now_loc]
        res = '1'
        now_loc -= 1
        while now_num != 0 and now_loc >= 0:
            if now_loc % 2 == 0:
                if now_num > neg[now_loc][0]:
                    res += '1'
                    now_num -= num[now_loc]
                else:
                    res += '0'
            else:
                if now_num < neg[now_loc][1]:
                    res += '1'
                    now_num -= num[now_loc]
                else:
                    res += '0'
            now_loc -= 1
        while now_loc >= 0:
            res += '0'
            now_loc -= 1
        return res

class Solution:
    def baseNegs(self, n: int) -> str:
        res = ''
        while n:
            n, k = -(n // 2), n % 2
            res = str(k) + res
        return res if res else '0'








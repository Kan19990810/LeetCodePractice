"""
给你一个仅由 0 和 1 组成的二进制字符串 s 。

如果子字符串中 所有的 0 都在 1 之前 且其中 0 的数量等于 1 的数量，则认为 s 的这个子字符串是平衡子字符串。请注意，空子字符串也视作平衡子字符串。

返回  s 中最长的平衡子字符串长度。

子字符串是字符串中的一个连续字符序列

"""
class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        n = len(s)
        i, j = 0, 0
        count0, count1 = 0, 0
        res = 0
        while i < n and s[i] == '1':
            i += 1
            j += 1
        while i < n:
            while i < n and s[i] == '0':
                i += 1
                j += 1
                count0 += 1
                #print(i, j)
            while j < n and s[j] == '1':
                j += 1
                count1 += 1
                #print(i, j)
            i = j
            res = max(res, 2 * min(count0, count1))
            #print(res)
            count0, count1 = 0, 0
        return res

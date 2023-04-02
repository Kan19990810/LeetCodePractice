"""
给你一个字符串 s ，一个字符 互不相同 的字符串 chars 和一个长度与 chars 相同的整数数组 vals 。

子字符串的开销 是一个子字符串中所有字符对应价值之和。空字符串的开销是 0 。

字符的价值 定义如下：

如果字符不在字符串 chars 中，那么它的价值是它在字母表中的位置（下标从 1 开始）。
比方说，'a' 的价值为 1 ，'b' 的价值为 2 ，以此类推，'z' 的价值为 26 。
否则，如果这个字符在 chars 中的位置为 i ，那么它的价值就是 vals[i] 。
请你返回字符串 s 的所有子字符串中的最大开销
"""
class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:
        n = len(s)
        if n == 0:
            return 0
        dp = [0] * (n + 1)
        d = dict(zip(chars, vals))
        res = dp[0]
        for i in range(1, n + 1):
            if s[i - 1] in d:
                dp[i] = dp[i - 1] + d[s[i - 1]]
                if dp[i] < 0:
                    dp[i] = 0
            else:
                dp[i] = dp[i - 1] + ord(s[i - 1]) - ord('a') + 1
            if dp[i] > res:
                res = dp[i]
        return res



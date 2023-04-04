"""
给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。
"""
from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        mem = defaultdict(int)
        for char in t:
            mem[char] += 1
        tLen = len(t)

        minLeft, minRight = 0, len(s)
        left = 0
        for right, char in enumerate(s):
            if mem[char] > 0:
                tLen -= 1
            mem[char] -= 1
            if tLen == 0:
                while mem[s[left]] < 0:
                    mem[s[left]] += 1
                    left += 1
                if right - left < minRight - minLeft:
                    minLeft, minRight = left, right
                mem[s[left]] += 1
                tLen += 1
                left += 1
        return '' if minRight == len(s) else s[minLeft:minRight + 1]


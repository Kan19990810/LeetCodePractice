"""
给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。

有效的 IP 地址 正好由四个整数（每个整数位于 0 到 255 之间组成，且不能含有前导 0），整数之间用 '.' 分隔。

例如："0.1.2.201" 和 "192.168.1.1" 是 有效的 IP 地址，但是 "0.011.255.245"、"192.168.1.312" 和 "192.168@1.1" 是 无效的 IP 地址。
"""
class Solution:
    def __init__(self):
        self.result = []

    def restoreIpAddresses(self, s: str) -> List[str]:
        self.result.clear()
        if len(s) > 12:
            return []
        self.backtracking(s, 0, 0)
        return self.result

    def backtracking(self, s: str, start_index: int, point_num: int) -> None:
        if point_num == 3:
            if self.is_valid(s, start_index, len(s) - 1):
                self.result.append(s[:])
            return
        for i in range(start_index, len(s)):
            if self.is_valid(s, start_index, i):
                s = s[:i + 1] + '.' + s[i + 1:]
                self.backtracking(s, i + 2, point_num + 1)
                s = s[:i + 1] + s[i + 2:]
            else:
                break
    def is_valid(self, s: str, start: int, end: int) -> bool:
        if start > end:
            return False
        if s[start] == '0' and start != end:
            return False
        if not 0 <= int(s[start:end + 1]) <= 255:
            return False
        return True
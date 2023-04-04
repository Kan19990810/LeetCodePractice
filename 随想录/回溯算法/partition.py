"""
给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。

返回 s 所有可能的分割方案。

示例: 输入: "aab" 输出: [ ["aa","b"], ["a","a","b"] ]
"""
class Solution:
    def __init__(self):
        self.paths = []
        self.path = []
    def partition(self, s: str) -> List[List[str]]:
        self.path.clear()
        self.paths.clear()
        self.backtracking(s, 0)
        return self.paths

    def backtracking(self, s: str, start_index: int) ->None:
        if start_index >= len(s):
            self.paths.append(self.path[:])
            return

        for i in range(start_index, len(s)):
            temp = s[start_index: i + 1]
            if temp == temp[::-1]:
                self.path.append(temp)
                self.backtracking(s, i + 1)
                self.path.pop()
            else:
                continue
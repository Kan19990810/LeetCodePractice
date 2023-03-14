"""
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
"""
class Solution:
    def __init__(self):
        self.answers: List[str] = []
        self.answer: str = ''
        self.letter_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }


    def letterCombinations(self, digits: str) -> List[str]:
        self.answers.clear()
        if not digits:
            return []
        self.backtracking(digits, 0)
        return self.answers


    def backtracking(self, digits: str, index: int) -> None:
        if index == len(digits):
            self.answers.append(self.answer)
            return
        letters: str = self.letter_map[digits[index]]
        for letter in letters:
            self.answer += letter
            self.backtracking(digits, index + 1)
            self.answer = self.answer[:-1]
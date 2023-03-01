"""
给定一个字符串，逐个翻转字符串中的每个单词。

示例 1：
输入: "the sky is blue"
输出: "blue is sky the"

示例 2：
输入: "  hello world!  "
输出: "world! hello"
解释: 输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。

示例 3：
输入: "a good   example"
输出: "example good a"
解释: 如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。
"""
class Solution:
    def trim_spaces(self, s):
        n = len(s)
        left = 0
        right = n - 1

        while left <= right and s[left] == ' ':
            left += 1
        while left <= right and s[right] == ' ':
            right -= 1
        tmp = []
        while left <= right:
            if s[left] != ' ':
                tmp.append(s[left])
            elif tmp[-1] != ' ':
                tmp.append(s[left])
            left += 1
        return tmp

    def reverse_string(self, nums, left, right):
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
            return None

    def reverse_each_word(self, nums):
        start = 0
        end = 0
        n = len(nums)
        while start < n:
            while end < n and nums[end] != ' ':
                end += 1
            self.reverse_string(nums, start, end - 1)
            start = end + 1
            end += 1
        return None

    def reverseWords(self, s):
        l = self.trim_spaces(s)
        self.reverse_string(l, 0, len(l) - 1)
        self.reverse_each_word(l)
        return ''.join(l)
    def reverseWords(self, s:str) -> str:
        s_list = [i for i in s.split(" ") if len(i) > 0]
        return " ".join(s_list[::-1])

        def trim_head_tail_space(ss: str):
            p = 0
            while p < len(ss) and ss[p] == " ":
                p += 1
            return ss[p:]

        s = trim_head_tail_space(s)
        s = trim_head_tail_space(s[::-1])[::-1]

        pf, ps, s = 0, 0, s[::-1]
        while pf < len(s):
            if s[pf] == " ":
                if s[pf] == s[pf + 1]:
                    s = s[:pf] + s[pf + 1 :]
                    continue
                else:
                    s = s[:ps] + s[ps: pf][::-1] + s[pf:]
                    ps, pf = pf + 1, pf + 2
            else:
                pf += 1
        return s[:ps] + s[ps:][::-1]

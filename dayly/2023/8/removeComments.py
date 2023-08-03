class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        # is_comment = False
        # comment_type = 0
        # n = len(source)
        # # 将所有行拼接
        # s = ''
        # for i in range(n):
        #     s += source[i]
        #     s += r'\n'

        # n = len(s)
        # ans = ''
        # first, second = 0, 1
        # while second < n:
        #     # 当遇到 // 时， 结束位为\n
        #     if s[second - 1: second + 1] == '//':
        #         # 当是第一次遇到 //
        #         if is_comment == False:
        #             is_comment = True
        #             # 将之前的字串填入
        #             ans += s[first: second - 1]
        #     # 当遇到 \n 时 需要判断之前是否遇到 //
        #     elif s[second - 1: second + 1] == r'\n' and is_comment == True and comment_type == 0:
        #         is_comment = False
        #         # 重新定位 first
        #         first = second - 1

        #     elif s[second - 1: second + 1] == '*/' and is_comment == True and comment_type == 1:
        #         is_comment = False
        #         comment_type = 0
        #         first = second + 1
        #         # 避免 *//
        #         second += 1

        #     # 当遇到 /*, 结束位为 */
        #     elif s[second - 1: second + 1] == '/*' and is_comment == False:
        #         is_comment = True
        #         comment_type = 1
        #         # 填入之前的字串
        #         ans += s[first: second - 1]
        #         # 避免 /*/
        #         second += 1

        #     second += 1
        # if first < n:
        #     ans += s[first::]
        # # 再处理ans 遇到 \n 则分开
        # res = []
        # n = len(ans)
        # idx = 0

        # for i in range(1, n):
        #     if ans[i - 1: i + 1] == r'\n':
        #         if len(ans[idx: i - 1]) != 0:
        #             res.append(ans[idx: i - 1])
        #         idx = i + 1
        # if idx < n:
        #     res.append(ans[idx::])

        # return res

        res = []
        new_line = []
        # /*  */ 标志位
        in_block = False
        # 每一行进行单独分析
        for line in source:
            i = 0
            while i < len(line):
                if in_block:
                    if i + 1 < len(line) and line[i] == '*' and line[i + 1] == '/':
                        in_block = False
                        i += 1
                else:
                    # 判断是否在 /*  */ 中， 避免标志位重叠
                    if i + 1 < len(line) and line[i] == '/' and line[i + 1] == '*':
                        in_block = True
                        i += 1
                    # 遇到// 直接跳过该行
                    elif i + 1 < len(line) and line[i] == '/' and line[i + 1] == '/':
                        break
                    else:
                        new_line.append(line[i])
                i += 1
                
            if  not in_block and len(new_line) > 0:
                res.append(''.join(new_line))
                new_line = []
        return res


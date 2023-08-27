class Solution:
    def getMaxFunctionValue(self, receiver: List[int], k: int) -> int:
        # 预处理闭环
        n = len(receiver)
        s = set()
        lines = []
        line_in = []
        # 每个玩家所在的环以及环的切入点
        for i in range(n):
            if i in s:
                continue
            else:
                j = i
                line = []
                while j not in s:
                    s.add(j)
                    line.append(j)
                    j = receiver[j]
                lines.append(line)
                line_in.append(j)

        cir_sum = []
        line_idx = []
        for i, x in enumerate(lines):
            idx = 0
            while x[idx] != line_in[i]:
                idx += 1
            line_idx.append(idx)
            cir_sum.append(sum(x[idx:]))
        # print(lines)
        # print(line_in)
        # print(cir_sum)
        # print(line_idx)
        # 计算f
        ans = 0
        for i in range(n):
            res = 0
            for idx, line in enumerate(lines):
                if i in line:
                    i_idx = 0
                    while i != line[i_idx]:
                        i_idx += 1
                    # print(i,i_idx)
                    if i_idx < line_idx[idx]:
                        if k <  line_idx[idx] - i_idx:
                            res = sum(line[i_idx:i_idx + k + 1])
                        else:
                            time = (k - line_idx[idx] + i_idx + 1) // (len(line) - line_idx[idx])
                            left = (k - line_idx[idx] + i_idx + 1) % (len(line) - line_idx[idx])
                            res = sum(line[i_idx: line_idx[idx]]) + cir_sum[idx] * time + sum(line[line_idx[idx]:line_idx[idx] + left])
                    else:
                        if k <= len(line) - i_idx:
                            res = sum(line[i_idx:i_idx + k + 1])
                        else:
                            time = (k - len(line) + i_idx + 1) // (len(line) - line_idx[idx])
                            left = (k - len(line) + i_idx + 1) % (len(line) - line_idx[idx])
                            res = sum(line[i_idx:]) + cir_sum[idx] * time + sum(line[line_idx[idx]:line_idx[idx] + left])
            ans = max(ans, res)
        return ans




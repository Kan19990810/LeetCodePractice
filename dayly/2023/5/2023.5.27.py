class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:
        result = [0] * 5
        i = 0
        while count[i] == 0:
            i += 1
        result[0] = i
        # print('mi', i)
        i = 255
        while count[i] == 0:
            i -= 1
        result[1] = i
        # print('ma', i)
        coun = sum(count)
        if coun % 2 == 0:
            idx1, idx2 = coun // 2, coun // 2
        else:
            idx1, idx2 = coun // 2, coun // 2 + 1
        pre, su, ma = 0, 0, 0
        for i, x in enumerate(count):
            if x == 0:
                continue
            result[2] += i * x / coun
            su += x
            if pre < idx1 <= su:
                result[3] += i
            if pre < idx1 <= su:
                result[3] += i
            pre = su
            if x > ma:
                result[4] = i
        result[3] //= 2
        return result





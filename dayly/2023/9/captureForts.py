class Solution:
    def captureForts(self, forts: List[int]) -> int:
        n = len(forts)
        pre = -1
        ans = 0
        for i in range(n):
            if pre == -1 and (forts[i] == -1 or forts[i] == 1):
                pre = i
            if pre != -1 and (forts[pre] == - forts[i]):
                ans = max(ans, i - pre - 1)
                pre = i
            if pre != -1 and (forts[pre] == forts[i]):
                pre = i
        return ans

class Solution:
    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
        ans = 0
        n = len(maxHeights)
        for idx, maxHeight in enumerate(maxHeights):
            res = maxHeight
            pre = maxHeight

            if idx > 0:
                for i in range(idx - 1, -1, -1):
                    pre = min(pre, maxHeights[i])
                    res += pre
            pre = maxHeight
            if idx < n - 1:
                for i in range(idx + 1, n):
                    pre = min(pre, maxHeights[i])
                    res += pre
            
            ans = max(ans, res)
            print(idx , res)
        return ans
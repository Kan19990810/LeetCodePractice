class Solution:
    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
        n = len(maxHeights)
        ans = 0

        stack = []

        re = [0] * n
        pre = [0] * n
        for i in range(n):
            while stack and maxHeights[stack[-1]] >= maxHeights[i]:
                stack.pop()
            if stack:
                idx = stack[-1]
                pre[i] = pre[idx] + maxHeights[i] * (i - idx)
            else:
                pre[i] = maxHeights[i] * (i + 1)
            stack.append(i)

        stack = []
        for i in range(n - 1, -1 , -1):
            while stack and maxHeights[stack[-1]] >= maxHeights[i]:
                stack.pop()
            if stack:
                idx = stack[-1]
                re[i] = re[idx] + maxHeights[i] * (idx - i)
            else:
                re[i] = maxHeights[i] * (n - i)
            stack.append(i)

        
        for i in range(n):
            ans = max(ans, pre[i] + re[i] - maxHeights[i])

        return ans
    #     n = len(maxHeights)
    #     stack = []
    #     ans = 0

    #     res = self.sumOfHeights(0, maxHeights[0], maxHeights)
    #     ans = max(ans, res)

    #     res = self.sumOfHeights(n - 1, maxHeights[n - 1], maxHeights)
    #     ans = max(ans, res)

    #     for i in range(n):
    #         st = False
    #         while stack and stack[-1] >= maxHeights[i]:
    #             if not st:
    #                 height = stack[-1]
    #                 st = True

    #                 res = self.sumOfHeights(i - 1, height, maxHeights)
                    
    #                 ans = max(ans, res)

    #             stack.pop()
            
    #         stack.append(maxHeights[i])

    #     stack = []
    #     for i in range(n - 1, -1 ,-1):
    #         st = False
    #         while stack and stack[-1] >= maxHeights[i]:
    #             if not st:
    #                 height = stack[-1]
    #                 st = True

    #                 res = self.sumOfHeights(i + 1, height, maxHeights)
                    
    #                 ans = max(ans, res)

    #             stack.pop()
            
    #         stack.append(maxHeights[i])

    #     return ans

    # def sumOfHeights(self, idx: int, height: int, maxHeights: List[int]) -> int:
    #     res = height
    #     pre = height
    #     n = len(maxHeights)
    #     if idx > 0:
    #         for i in range(idx - 1, -1, -1):
    #             pre = min(pre, maxHeights[i])
    #             res += pre
    #     pre = height
    #     if idx < n - 1:
    #         for i in range(idx + 1, n):
    #             pre = min(pre, maxHeights[i])
    #             res += pre
    #     return res
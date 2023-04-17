class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)

        prefix = [height[0]] * n
        suffix = [height[n - 1]] * n
        ans = 0

        for i in range(1, n):
            prefix[i] = max(prefix[i- 1], height[i])

        for i in range(n - 2, -1, -1):
            suffix[i] = max(suffix[i + 1], height[i])

        for i in range(1, n - 1):
            ans += min(prefix[i], suffix[i]) - height[i]

        return ans


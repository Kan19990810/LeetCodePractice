class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        left, right = 0, n - 1
        ans = min(height[left], height[right]) * (n - 1)

        while left < right:
            if height[left] <= height[right]:
                left += 1

            else:
                right -= 1

            ans = max(ans, min(height[left], height[right]) * (right - left))

        return ans
class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        n = len(obstacles)
        g = []
        ans = []
        for i in obstacles:
            left, right = 0, len(g) - 1
            while left <= right:
                mid = (left + right) // 2
                if i >= obstacles[mid]:
                    left = mid + 1
                else:
                    right = mid - 1

            if left == len(g):
                g.append(i)
            else:
                g[left] = i
            ans.append(left + 1)
            print(g)
        return ans

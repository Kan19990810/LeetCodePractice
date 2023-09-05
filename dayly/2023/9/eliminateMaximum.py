class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        ans = 0

        n = len(dist)
        time = [0] * n
        for i in range(n):
            # 5 // 2 = 2 在第 2 分钟及之前需要消灭
            # 4 // 2 = 2 在第2 分钟之前需要消灭
            time[i] = dist[i] // speed[i] if dist[i] % speed[i] > 0 else dist[i] // speed[i] - 1

        time.sort()

        for i in range(n):
            if i <= time[i]:
                ans += 1
            else:
                break

        return ans
class Solution:
    def sumDistance(self, nums: List[int], s: str, d: int) -> int:
        place = list(sorted(zip(nums, s), key=lambda p: p[0]))

        n = len(nums)
        ans = 0
        for i in range(n):
            ans += (2 * i - n + 1) * place[i][0]
            ans %= 10 ** 9 + 7

        if place[0][1] == 'L':
            left = place[0][0] - d
        else:
            i = 1
            while place[i][1] != 'L':
                i += 1
            if i < n:
                if d < (place[i][0] - place[0][0]) // 2:
                    left = place[0][0] + d
                else:
                    left = place[i][0] - d

            else:
                left = place[0][0] + d

        if place[n - 1][1] == 'R':
            right = place[n - 1][0] + d
        else:
            i = n - 2
            while place[i][1] != 'R':
                i -= 1
            if i > -1:
                if d < (place[n - 1][0] - place[i][0]) // 2:
                    right = place[n - 1][0] - d
                else:
                    right = place[i][0] + d
            else:
                right = place[n - 1][0] - d
        return ans + (n - 1) * (place[0][0] - left) + (n - 1) * (right - place[n - 1][0])



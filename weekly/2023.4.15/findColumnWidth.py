class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:

        ans = [0] * len(grid[0])

        for _, row in enumerate(grid):
            for i, num in enumerate(row):
                width = 1

                if num >= 0:
                    while num > 9:
                        num //= 10
                        width += 1
                    ans[i] = max(ans[i], width)
                else:
                    num *= -1
                    width += 1
                    while num > 9:
                        num //= 10
                        width += 1
                    ans[i] = max(ans[i], width)

        return ans




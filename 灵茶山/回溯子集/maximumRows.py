class Solution:
    def maximumRows(self, matrix: List[List[int]], numSelect: int) -> int:
        row = len(matrix)
        col = len(matrix[0])

        ans, num, numS = 0, 0, numSelect

        def dfs(i):
            nonlocal ans
            nonlocal num
            nonlocal numS

            if i == col or numS == 0:
                num = 0
                print(matrix)
                for n in range(row):
                    if all(matrix[n][m] == 0 for m in range(col)):
                        num += 1
                ans = max(ans, num)
                return

            dfs(i + 1)
            cnt = [0] * row
            for n in range(row):
                cnt[n] = matrix[n][i]
                matrix[n][i] = 0
            numS -= 1
            # print(matrix)

            dfs(i + 1)
            for n in range(row):
                matrix[n][i] = cnt[n]
            numS += 1

        dfs(0)
        return ans
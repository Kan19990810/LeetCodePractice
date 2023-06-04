class Solution:
    def matrixSumQueries(self, n: int, queries: List[List[int]]) -> int:
        # num = [[0] * n for _ in range(n)]
        # for i in queries:
        #     if i[0] == 0:
        #         for col in range(n):
        #             num[i[1]][col] = i[2]
        #     else:
        #         for row in range(n):
        #             num[row][i[1]] = i[2]
        # ans = 0
        # for i in num:
        #     ans += sum(i)
        # return ans
        a = len(queries)
        row, col = [0] * n, [0] * n
        rowNum, colNum = 0, 0
        ans = 0
        for i in range(a - 1, -1, -1):
            if queries[i][0] == 0 and row[queries[i][1]] == 0:
                ans += queries[i][2] * (n - rowNum)
                row[queries[i][1]] = 1
                colNum += 1

            if queries[i][0] == 1 and col[queries[i][1]] == 0:
                ans += queries[i][2] * (n - colNum)
                col[queries[i][1]] = 1
                rowNum += 1

        return ans

class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        count, ma = 0, 0

        ans = [0, 0]

        for i, row in enumerate(mat):
            count = 0
            for _, num in enumerate(row):
                if num == 1:
                    count += 1

            if count > ma:
                ma = count
                ans = [i, ma]

        return ans

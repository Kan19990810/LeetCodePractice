class Solution:
    def minimumPossibleSum(self, n: int, target: int) -> int:

            ma = target // 2
            if n <= ma:
                return sum(i for i in range(1, n + 1))
            else:
                return sum(i for i in range(1, ma + 1)) + sum(i for i in range(target, target + n - ma))

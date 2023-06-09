class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        def dfs(i, left):
            if i == 0:
                if left % 2 != 0 or left < 0:
                    return -inf
                else:
                    return 0

            if left % 2 != 0:
                return max(dfs(i - 1, left), dfs(i, left - 1) + prices[i])
            else:
                return max(dfs(i - 1, left), dfs)
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        n = len(nums)

        def dfs(i, s):
            if i == n:
                res.append(path.copy())
                return

            for ele in s:
                path.append(ele)
                dfs(i + 1, s - {ele})
                path.pop()

        dfs(0, set(nums))
        return res
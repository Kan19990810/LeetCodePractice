class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:
        n = len(nums)
        score = [0] * n
        ans = [0] * n
        ma = 0

        for i, num in enumerate(nums):
            if i == 0:
                ma = max(ma, num)
                score[i] = num + ma
                ans[i] = score[i]
            else:
                ma = max(ma, num)
                score[i] = num + ma
                ans[i] = score[i] + ans[i - 1]
        return ans

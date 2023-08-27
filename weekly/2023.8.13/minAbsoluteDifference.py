class Solution:
    def minAbsoluteDifference(self, nums: List[int], x: int) -> int:
        n = len(nums)
        num_idx = [[nums[i],i] for i in range(n)]
        num_idx.sort(key=lambda x: x[0])
        ans = inf 
        for i in range(n):
            # 最差答案 都不满足要求
            if num_idx[-1][0] - num_idx[i][0] < ans:
                continue
            j = i
            while j <= n - 1 and abs(num_idx[i][1] - num_idx[j][1]) < x and num_idx[j][0] - num_idx[i][0] < ans:
                j += 1
            if j <= n - 1:
                ans = min(ans, num_idx[j][0] - num_idx[i][0]) 
        return ans
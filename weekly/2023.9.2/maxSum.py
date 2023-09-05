from collections import Counter
class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        n = len(nums)
        ans = 0
        s = Counter(nums[:k])

        if len(s) >= m:
            ans = sum(nums[:k])
        # 减去 i 加入 i + k  
        for i in range(n - k):
            s[nums[i]] -= 1
            if s[nums[i]] == 0:
                del s[nums[i]]
            s[nums[i + k]] += 1
            if len(s) >= m:
                ans = max(ans, sum(nums[i + 1: i + k + 1]))

        return ans


        

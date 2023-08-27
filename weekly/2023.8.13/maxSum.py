class Solution:
    def maxSum(self, nums: List[int]) -> int:
        n = len(nums)
        ans = -1
        for i in range(n):
            a = nums[i]
            i_max = 0
            while a > 0:
                i_max = max(i_max, a % 10)
                a //= 10

            for j in range(i + 1, n):
                b = nums[j]
                j_max = 0
                while b > 0:
                    j_max = max(j_max, b % 10)
                    b //= 10
                
                if i_max == j_max:
                    ans = max(ans, nums[i] + nums[j])
        
        return ans
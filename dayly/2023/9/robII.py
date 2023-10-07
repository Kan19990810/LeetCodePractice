class Solution:
    def rob(self, nums: List[int]) -> int:
        # # 动规规划

        # n = len(nums) - 1

        # if n == 0:
        #     return nums[0]

        # dp = [[0] * 2 for i in range(n)]

        # dp[0][1] = nums[0]
        # for i in range(1, n):
        #     # 第 i 家不偷
        #     dp[i][0] = max(dp[i - 1][0], dp[i - 1][1])

        #     # 第 i 家偷
        #     dp[i][1] = max(dp[i - 1][0], dp[i - 2][1]) + nums[i]

        # st =  max(dp[n - 1][0], dp[n - 1][1])

        # dp = [[0] * 2 for i in range(n)]

        # dp[0][1] = nums[1]
        # for i in range(1, n):
        #     # 第 i 家不偷
        #     dp[i][0] = max(dp[i - 1][0], dp[i - 1][1])

        #     # 第 i 家偷
        #     dp[i][1] = max(dp[i - 1][0], dp[i - 2][1]) + nums[i + 1]

        # st = max(st, max(dp[n - 1][0], dp[n - 1][1]))

        # return st

        def robrange(start, end) -> int:
            first = nums[start]
            second = max(nums[start], nums[start + 1])
            for i in range(start + 2,  end + 1):
                first , second = second , max(first + nums[i], second)
            return second
        
        length = len(nums)
        if length == 1:
            return nums[0]
        elif length == 2:
            return max(nums[0], nums[1])
        else:
            return max(robrange(0, length - 2), robrange(1, length - 1))
        

class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        # 暴力遍历

        ans = 0
        for i in range(total // cost1 + 1):
            left = total - cost1 * i
            ans += left // cost2 + 1
            # print(i, left // cost2)
        return ans
    
        # 动规 dp[i] 为 total = i 时的方案数
        # 转移公式 dp[i] =  dp[i - cost1] + dp[i - cost2] + 2
        dp = [0] * (total + 1)

        dp[0] = 1

        for i in range(1, total + 1):
            if i < cost1 and i < cost2:
                dp[i] = dp[i - 1]
            if i >= cost1 and i < cost2:
                dp[i] = dp[i - cost1] + 1
            if i < cost1 and i >= cost2:
                dp[i] = dp[i - cost2] + 1
            if i >= cost1 and i >= cost2:
                dp[i] = dp[i - cost1] + dp[i - cost2] + 2

        return dp[total]

      
        if cost1 < cost2:
            return self.waysToBuyPensPencils(total, cost2, cost1)
        res, cnt = 0, 0
        while cnt * cost1 <= total:
            res += (total - cnt * cost1) // cost2 + 1
            cnt += 1
        return res


class Solution:
    def sumOfPower(self, nums: List[int]) -> int:
        """
        10 ^ 5 表明无法直接用递归暴力
        max ^ 2 * min
        利用有序性
        不止前缀和
        固定最大值， 寻找最小值的组合
        [1] 
        min: 2 ^ 0 * nums[0] max: nums[1] 
        [1, 2] [1] [2]
        min: 2 ^ 1 * nums[0] + 2 ^ 0 * nums[1] max: nums[2]
        [1, 2, 3] [1, 2] [1, 3] [2, 3] [1] [2] [3]
        min: 2 ^ 2 * nums[0] + 2 ^ 1 * nums[1] + 2 ^ 0 nums[2] max: nums[3]
        [2 * 2] [2] [1]
        对于只含一个数的组合 [1] [2] [3]
        [1] ^ 3  [2] ^ 3
        """
        MOD = 10 ^ 9 + 7
        # 排序
        n = len(nums)
        nums.sort()
        # 前缀
        cum = [0] * n
        cum[0] = nums[0]
        for i in range(1, n):
            cum[i] = 2 * cum[i - 1] + nums[i]
            cum[i] %= MOD
        # 求和
        ans = 0
        for i in range(n - 1):
            ans += nums[i + 1] ^ 2 * cum[i]
            ans %= MOD
        for i in range(n):
            ans += pow(nums[i], 3)
            ans %= MOD
        return ans
        
class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        # # 考虑正负关系
        # # 双指针 区间为正 记录遇到的第一个负数
        # n = len(nums)
        # first, second, s, res = 0, 0, 0, 0
        # buff, time = False, False
        
        # if nums[0] >= 0:
        #     buff = True

        # # 正 - 负  = 正:  正 > 负 
        # while second < n:
        #     s += nums[second]
        #     res = max(res, abs(s))
        #     # 第一次遇到不同符号的数, 记录该数的位置
        #     if ((nums[second] >= 0 and not buff) or (nums[second] < 0 and buff)) and not time:
        #         first = second
        #         time = True

        #     # 正负号发生变化
        #     if (s >= 0 and not buff) or (s < 0 and buff):
        #         second = first
        #         if nums[first] >= 0:
        #             buff = True
        #         else:
        #             buff = False
        #         s = 0
        #         time = False
        #     # 正负号没有发生变化
        #     else:
        #         second += 1
        # return res
        # 动态规划
        positiveMax, negativeMin = 0, 0
        positiveSum, negativeSum = 0, 0
        for n in nums:
            positiveSum += n
            positiveMax = max(positiveMax, positiveSum)
            positiveSum = max(0, positiveSum)

            negativeSum += n
            negativeMin = min(negativeMin, negativeSum)
            negativeSum = min(0, negativeSum)
        return max(positiveMax, -negativeMin)
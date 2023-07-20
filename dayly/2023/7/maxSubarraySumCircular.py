class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        leftMax = [0] * n
        # 对坐标为 0 处的元素单独处理，避免考虑子数组为空的情况
        leftMax[0], leftSum = nums[0], nums[0] 
        pre, res = nums[0], nums[0]
        for i in range(1, n):
            # pre, res 为连续数组时的情况
            pre = max(pre + nums[i], nums[i])
            res = max(res, pre)
            leftSum += nums[i]
            leftMax[i] = max(leftMax[i - 1], leftSum)
        # 从右到左枚举后缀，固定后缀，选择最大前缀
        rightSum = 0
        for i in range(n - 1, 0, -1):
            rightSum += nums[i]
            res = max(res, rightSum + leftMax[i - 1])
        return res


        

        # cum = [0] * 2 * n
        # # 前缀和
        # for i in range(2 * n):
        #     cum[i] = cum[i - 1] + nums[i % n]

        # # 双指针
        # first, second = 0, 0
        # while second < 2 * n:
        #     if second < 2 * n - 1 and cum[second] < cum[second + 1]:
        #         second += 1
        #     m = 
        #     for j in range(first, second):
                




        # # 前缀和排序
        # sortCum = [i for i in range(2 * n)]
        # sortCum.sort(key = lambda i: cum[i])
        # # print(cum, sortCum)
        # ans = -inf
        # idx = 2 * n - 1
        # # 满足数组长度小于n, 前缀和最大值减去前缀和最小值
        # for second in range(2 * n - 1, -1, -1):
        #     first = 0
        #     # 如何避免 second = first
        #     # 长度范围为 [1, n]
        #     while (sortCum[second] - sortCum[first] > n or sortCum[second] - sortCum[first] < 0) and first < idx:
        #         first += 1
        #     if first != second:
        #         ans = max(ans, cum[sortCum[second]] - cum[sortCum[first]])
        #         idx = first
        #     else:
        #         ans = max(ans, nums[second % n])
        #         idx = second - 1

        # return ans

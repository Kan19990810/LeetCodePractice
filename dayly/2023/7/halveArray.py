import heapq
class Solution:
    def halveArray(self, nums: List[int]) -> int:
        # 10 ^ 5 不能暴力
        # 贪心 每次操作 最大的数
        # 维护一个单调栈？



        pq = []
        for num in nums:
            heapq.heappush(pq, -num)
        res = 0
        sum1 = sum(nums)
        sum2 = 0
        while sum2 < sum1 / 2:
            x = -heapq.heappop(pq)
            sum2 += x / 2
            heapq.heappush(pq, -(x / 2))
            res += 1
        return res

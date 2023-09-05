class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        # 记录有趣数的下标
        interest_index = []
        n = len(nums)
        interest_index.append(-1)
        for i in range(n):
            if nums[i] % modulo == k:
                interest_index.append(i)
        interest_index.append(n)
        # 有趣数下标  a b c d 
        # 10 ** 5 不能暴力 [l, r] 
        # 有趣数的前缀和？ 

        m = len(interest_index)
        ans = 0
        # 遍历每个坐标 作为右端点
        for i in range(1, m):
            # 计算左端点有几个 time = n 则至多 n + 1个左端点
            time = (i - 1) // modulo
            for j in range(time + 1):
                #  j = i - modulo * j - k
                #  考虑一下边界问题
                if i - modulo * j - k - 1 >= 0:
                    ans += interest_index[i] - interest_index[i - modulo * j - k] - 1

        return ans

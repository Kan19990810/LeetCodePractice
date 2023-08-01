from collections import Counter 
class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        ans = 0
        num = set(nums)
        n = len(nums)
        nnum = len(num)
        # 找到以 nums[i]为结尾的最短完全子数组
        for i in range(n):
            # 剪枝
            if i + 1 < nnum:
                continue
            # j 最大从 i - nnum + 1开始
            j = i - nnum + 1
            # 统计nums[j: i + 1]的不同数个数
            s = set(nums[j:i + 1])
            # j > 0 当j = 0的时候就说明没有其他的数了
            # 当不同数满足完全子数组时，之前的数都可以了
            while j > 0 and len(s) < nnum:
                j -= 1
                s.add(nums[j])
            if len(s) == nnum:
                ans += j + 1
            print(ans, j, i)
        return ans
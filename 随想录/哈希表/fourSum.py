"""
给你一个由 n 个整数组成的数组 nums ，和一个目标值 target 。请你找出并返回满足下述全部条件且不重复的四元组 [nums[a], nums[b], nums[c], nums[d]] （若两个四元组元素一一对应，则认为两个四元组重复）：

0 <= a, b, c, d < n
a、b、c 和 d 互不相同
nums[a] + nums[b] + nums[c] + nums[d] == target
你可以按 任意顺序 返回答案 。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/4sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]: continue
            for k in range(i + 1, n):
                if k > i + 1 and nums[k] == nums[k - 1]:continue
                p = k + 1
                q = n - 1
                while p < q:
                    if nums[i] + nums[k] + nums[p] + nums[q] > target: q -= 1
                    elif nums[i] + nums[k] + nums[p] + nums[q] < target: p += 1
                    else:
                        res.append([nums[i],nums[k],nums[p],nums[q]])
                        while p < q and nums[p] == nums[p + 1]: p += 1
                        while p < q and nums[q] == nums[p - 1]: q -= 1
                        p += 1
                        q -= 1
        return res

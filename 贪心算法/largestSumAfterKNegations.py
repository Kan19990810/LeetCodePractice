"""
给定一个整数数组 A，我们只能用以下方法修改该数组：我们选择某个索引 i 并将 A[i] 替换为 -A[i]，然后总共重复这个过程 K 次。（我们可以多次选择同一个索引 i。）

以这种方式修改数组后，返回数组可能的最大和。
"""
class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums = sorted(nums, key=abs, reverse=True)
        for i in range(len(nums)):
            if (k > 0) and (nums[i] < 0):
                nums[i] *= -1
                k -= 1
        if k > 0:
            nums[-1] *= (-1) ** k
        return sum(nums)


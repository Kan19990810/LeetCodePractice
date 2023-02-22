"""
给定两个数组 nums1 和 nums2 ，返回 它们的交集 。输出结果中的每个元素一定是 唯一 的。我们可以 不考虑输出结果的顺序
"""

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        val_dict = {}
        ans = []
        for num in nums1:
            val_dict[num] = 1
        for num in nums2:
            if num in val_dict.keys() and val_dict[num] == 1:
                ans.append(num)
                val_dict[num] =0
        return ans
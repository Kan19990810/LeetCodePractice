"""
给你一个整数数组 nums 。请你创建一个满足以下条件的二维数组：

二维数组应该 只 包含数组 nums 中的元素。
二维数组中的每一行都包含 不同 的整数。
二维数组的行数应尽可能 少 。
返回结果数组。如果存在多种答案，则返回其中任何一种。

请注意，二维数组的每一行上可以存在不同数量的元素。
"""
from collections import Counter






class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        dict = {}
        n = len(nums)
        i, j, m = 0, 0, 0
        for num in nums:
            dict[num] = 0
        for num in nums:
            dict[num] += 1
            m = max(m, dict[num])
        res = [[] for _ in range(m)]
        for i in range(m):
            for num in dict:
                if dict[num] > 0:
                    res[i].append(num)
                    j += 1
                    dict[num] -= 1
            j = 0
        return res


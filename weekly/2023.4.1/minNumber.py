"""
给你两个只包含 1 到 9 之间数字的数组 nums1 和 nums2 ，每个数组中的元素 互不相同 ，请你返回 最小 的数字，两个数组都 至少 包含这个数字的某个数位。
"""
from typing import List
class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        num1, num2 = sorted(nums1), sorted(nums2)
        n, m = len(nums1), len(nums2)
        i, j = 0, 0
        while i < n:
            print(i, j)
            if num1[i] == num2[j]:
                return num1[i]
            elif num1[i] > num2[j]:
                if j == m - 1:
                    break
                j += 1
            else:
                i += 1
        if num1[0] < num2[0]:
            return num1[0] * 10 + num2[0]
        return num2[0] * 10 + num1[0]






"""
给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素，并返回移除后数组的新长度。

不要使用额外的数组空间，你必须仅使用 O(1) 额外空间并原地修改输入数组。

元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。
"""
class Solution:
    def removeElemt_1(self, nums: List[int], val: int) -> int:
        i = 0
        size = len(nums)

        while i < size:
            if nums[i] == val:
                for j in range(i, size - 1):
                    nums[j] = nums[j + 1]
                if i > 0:
                    i -= 1
                    size -= 1
                else:
                    size -= 1
            else:
                i += 1

        return size

    def removeElemt_2(self, nums: List[int], val: int) -> int:
        fast = 0
        slow = 0
        size = len(nums)
        while fast < size:
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow

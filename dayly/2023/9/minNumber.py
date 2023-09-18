class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        s1 = set(nums1)
        s2 = set(nums2)
        
        s = s1 & s2
        if len(s) >0:
            return min(s)
        else:
            return min(min(s1) * 10 + min(s2), min(s2) * 10 + min(s1))
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        ans = [0] * (n + m)
        i, j = 0, 0
        while i < m and j < n:
            if nums1[i] <= nums2[j]:
                ans[i + j] = nums1[i]
                i += 1
            else:
                ans[i + j] = nums2[j]
                j += 1

        if i < m:
            ans[i + j :] = nums1[i: m]
        if j < n:
            ans[i + j :] = nums2[j: n]
        
        for i in range(n + m):
            nums1[i] = ans[i]
        
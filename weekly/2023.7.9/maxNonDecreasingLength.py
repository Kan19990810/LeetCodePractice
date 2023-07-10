import heapq


class Solution:
    def maxNonDecreasingLength(self, nums1: List[int], nums2: List[int]) -> int:
        # n, res = len(nums1), 1
        # heap = []
        # nums3 = [0] * n
        # nums3[0] = min(nums1[0], nums2[0])
        # heapq.heappush(heap, max(nums1[0], nums2[0]))
        # for i in range(1, n):
        #     if nums1[i] > nums3[i - 1]:
        #         heapq.heappush(heap, nums1[i])
        #     if nums2[i] > nums3[i - 1]:
        #         heapq.heappush(heap, nums2[i])
        #
        #     k = 0
        #     while len(heap) > 0 and k < nums3[i - 1]:
        #         k = heapq.heappop(heap)
        #
        #     if k >= nums3[i - 1]:
        #         nums3[i] = k
        #         res += 1
        #     else:
        #         return res
        #
        # return res

        n, ans = len(nums1), 1
        j = 0
        for j in range(n):
            nums3 = [0] * n
            res = 0
            for i in range(j, n):
                if nums1[i] >= nums3[i - 1] and nums2[i] >= nums3[i - 1]:
                    nums3[i] = min(nums1[i], nums2[i])
                    res += 1
                elif nums1[i] >= nums3[i - 1]:
                    nums3[i] = nums1[i]
                    res += 1
                elif nums2[i] >= nums3[i - 1]:
                    nums3[i] = nums2[i]
                    res += 1
                else:
                    ans = max(ans, res)
                    break
                if i == n - 1:
                    ans = max(ans, res)

        return ans

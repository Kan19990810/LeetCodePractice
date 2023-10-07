class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        # n = len(nums)
        # i, j, k = 0, 1, 2
        # ans = (nums[i] - nums[j]) * nums[k]
        # for idx in range(3, n):
        #     if nums[idx] >= nums[k]:
        #         k = idx
        #         ans = max(ans, (nums[i] - nums[j]) * nums[k])
        #     if nums[idx - 1] <= nums[j]:
        #         j = idx - 1
        #         k = idx
        #         ans = max(ans, (nums[i] - nums[j]) * nums[k])
        #     if nums[idx - 2] >= nums[i]:
        #         i = idx - 2
        #         j = idx - 1
        #         k = idx
        #         ans = max(ans, (nums[i] - nums[j]) * nums[k])
        # return ans if ans >0 else 0
        # ans = 0
        # n = len(nums)
        # mi = nums[1]
        # mi_idx = []
        # for idx in range(1, n - 1):
        #     if nums[idx] < mi:
        #         mi = nums[idx]
        #         mi_idx = [idx]
        #     elif nums[idx] == mi:
        #         mi_idx.append(idx)

        # for idx in mi_idx:
        #     pre_ma = max(nums[0: idx])
        #     pos_ma = max(nums[idx + 1 : n])
        #     ans = max(ans, (pre_ma - mi) * pos_ma)

        # return ans if ans > 0 else 0

        ans = 0
        n = len(nums)

        ma_diff = 0
        i, j = 0, 1
        while j < n - 1:
            if nums[j - 1] > nums[i]:
                i = j - 1

            if nums[i] - nums[j] > ma_diff:
                ma_diff = nums[i] - nums[j]
                ans = maxs(ans, ma_diff * max(nums[j + 1:]))

            j += 1

        return ans if ans > 0 else 0

            
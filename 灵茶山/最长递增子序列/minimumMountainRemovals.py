class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        forward = []
        backward = []
        forlen = [0] * n
        backlen = [0] * n
        for i in range(n):
            left, right = 0, len(forward) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[i] > forward[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
            if left == len(forward):
                forward.append(nums[i])
            else:
                forward[left] = nums[i]
            forlen[i] = left + 1
            # print(forward)
            left, right = 0, len(backward) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[-1 - i] > backward[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
            if left == len(backward):
                backward.append(nums[-1 - i])
            else:
                backward[left] = nums[-1 - i]
            backlen[i] = left + 1
        i = 0
        while forlen[i] == 1:
            forlen[i] = 0
            i += 1
        i = 0
        while backlen[i] == 1:
            backlen[i] = 0
            i += 1
        ans = [0] * n
        for i in range(n):
            if forlen[i] != 0 or backlen[i] != 0:
                ans[i] = forlen[i] + backlen[- 1 - i]
            else:
                ans[i] = -inf
        return n - max(ans) + 1


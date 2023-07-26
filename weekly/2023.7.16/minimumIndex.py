from collections import Counter


class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        n = len(nums)
        C = Counter(nums)
        time = 0
        for key in C:
            # print(key, C[key])
            if C[key] > time:
                time = C[key]
                x = key

        # print(C,x,time)
        num = 0
        for i in range(n):
            if nums[i] == x:
                num += 1

            if num * 2 > i + 1 and (time - num) * 2 > n - i - 1:
                return i

        return -1

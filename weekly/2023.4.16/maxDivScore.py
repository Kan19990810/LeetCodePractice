class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        divisors.sort()

        ans = [divisors[0], 0]

        for i, divisor in enumerate(divisors):
            count = 0

            for _, num in enumerate(nums):

                if num % divisor == 0:
                    count += 1

            if count > ans[1]:
                ans = [divisors[i], count]

        return ans[0]

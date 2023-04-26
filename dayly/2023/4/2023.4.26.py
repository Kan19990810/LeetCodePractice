class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        n = len(nums)
        firstLen = max(firstLen, secondLen)
        secondLen = min(firstLen, secondLen)

        firSum = [0] * (n - firstLen + 1)
        secSum = [0] * (n - secondLen + 1)
        for i in range(n - firstLen + 1):
            for j in range(firstLen):
                firSum[i] += nums[i + j]
        for i in range(n - secondLen + 1):
            for j in range(secondLen):
                secSum[i] += nums[i + j]

        ans = 0
        for i in range(n - firstLen - secondLen + 1):
            for j in range(i + 1, n - secondLen + 1):
                ans = max(ans, firSum[i] + secSum[j])

        for i in range(n - firstLen - secondLen + 1):
            for j in range(i + 1, n - firstLen + 1):
                ans = max(ans, secSum[i] +firSum[j])

        return ans

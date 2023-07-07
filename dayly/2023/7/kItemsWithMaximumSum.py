class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        ans = 0
        if k <= numOnes:
            ans = k
        elif numOnes < k <= numOnes + numZeros:
            ans = numOnes
        else:
            ans = 2 * numOnes + numZeros - k
        return ans
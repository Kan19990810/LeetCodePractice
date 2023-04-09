class Solution:
    def isPrime(self, num: int) -> bool:
        if num == 1:
            return False
        i = 2
        while i * i <= num:
            if num % i == 0:
                return False
            i += 1
        return True
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        n = len(nums)
        ma = 0
        for i in range(n):
            if self.isPrime(nums[i][i]):
                if nums[i][i] > ma:
                    ma = nums[i][i]
            if self.isPrime(nums[i][n - i - 1]):
                if nums[i][n - i - 1] > ma:
                    ma = nums[i][n - i - 1]
        return ma





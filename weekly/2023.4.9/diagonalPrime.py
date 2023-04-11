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

def is_prime(n: int) -> bool:
    i = 2
    while i * i < n:
        if n % i == 0:
            return False
    return n >= 2

class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        ans = 0
        for i, row in enumerate(nums):
            for x in row[i], row[-1 - i]:
                if x > ans and is_prime(x):
                    ans = max(ans, x)
        return ans




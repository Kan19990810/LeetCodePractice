from collections import Counter
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        s = Counter(nums)
        ans = 0
        for num in s:
            times = s[num]
            if times == 1:
                return -1
            
            res = times // 3
            left = times % 3
            res += (left + 1) // 2
            ans += res
        return ans
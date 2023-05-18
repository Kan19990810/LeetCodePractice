class Solution:
    def countElements(self, nums: List[int]) -> int:
        count = Counter(nums)
        return len(nums) - count[max(nums)] - count[min(nums)] if max(nums) != min(nums) else len(nums) - count[max(nums)]

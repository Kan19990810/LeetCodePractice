
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        ans = nums[0] + nums[1] + nums[2]

        for i in range(n):
            j = i + 1
            k = n - 1

            while j < k:
                cur = nums[i] + nums[j] + nums[k]

                if cur > target:
                    k -= 1
                    if abs(cur - target) < abs(ans - target):
                        ans = cur
                elif cur < target:
                    j += 1
                    if abs(cur - target) < abs(ans - target):
                        ans = cur
                else:
                    return cur
        return ans



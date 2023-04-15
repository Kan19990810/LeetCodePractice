class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []

        for a in range(n - 3):
            if a > 0 and nums[a] == nums[a - 1]:
                continue

            for b in range(a + 1, n - 2):

                if b > a + 1 and nums[b] == nums[b - 1]:
                    continue

                c = b + 1
                d = n - 1

                while c < b:
                    s = nums[a] + nums[b] + nums[c] + nums[d]

                    if s > target:
                        d -= 1
                    elif s < target:
                        c += 1
                    else:
                        ans.append([nums[a], nums[b], nums[c], nums[d]])
                        print(ans)
                        while c < b and nums[c] == nums[c + 1]:
                            c += 1
                        while c < b and nums[d] == nums[d - 1]:
                            d -= 1
                        c += 1
                        d -= 1
        return ans




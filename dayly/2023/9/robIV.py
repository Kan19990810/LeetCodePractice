class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        # 二分查找
        n = len(nums)
        left, right = min(nums), max(nums)
        
        while left < right:
            mid = (left + right) >> 1
            if self.valid(mid, nums, k): right = mid;
            else: left = mid + 1

        return left

    def valid(self, mid: int, nums: List[int], k: int) -> bool:
        n = len(nums)
        st = False
        t = 0
        for i in range(n):
            if not st and nums[i] <= mid:
                st = True
                t += 1
            else:
                st = False

        if t >= k:
            return True
        else:
            return False

        # # 回溯

        # n = len(nums)
        # res = []
        # ans = inf


        # def bfs(i, st):
        #     nonlocal ans

        #     if i == n:
        #         if len(res) >= k:
        #             t = max(res)
        #             ans = min(t, ans)
        #         return 

        #     if st:
        #         res.append(nums[i])
        #         bfs(i + 1, False)
        #         res.pop()
        #     else:
        #         bfs(i + 1, False)
        #         bfs(i + 1 ,True)

        
        # bfs(0, True)
        # bfs(0, False)

        # return ans
            


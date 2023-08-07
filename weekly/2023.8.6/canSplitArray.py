class Solution:
    def canSplitArray(self, nums: List[int], m: int) -> bool:
        # 连续子数组
        # 拆分为长度为1 或者 和大于 m
        # 拆分的话只能拆两端
        # 贪心不对
        @cache
        def dfs(i, j, s):
            if s < m:
                return False
            if i + 1 >= j:
                return True 
            
            return dfs(i + 1, j, s - nums[i]) or dfs(i, j - 1, s - nums[j])
            
        n = len(nums)
        s = sum(nums)
        first, second = 0, n - 1
        # 前后两端进行 相向双指针
        # 结束条件 [first,  ,second]
        # while (first + 1 < second ):
        #     # 贪心 拆最小的出去
        #     # nums[first] == nums[second]的情况需要递归
        #     if nums[first] < nums[second]:
        #         s -= nums[first]
        #         first += 1
        #     else:
        #         s -= nums[second]
        #         second -= 1
        #     if s < m:
        #         return False
        # return True
        if first + 1 >= second:
            return True
        return dfs(first, second, s)
    
        def dfs(i, j, s):
            if i + 1 >= j:
                return True 
            if s < m:
                return False
            
            if nums[i] < nums[j]:
                return dfs(i + 1, j, s - nums[i])
            elif nums[i] > nums[j]:
                return dfs(i, j - 1, s - nums[j])
            else:
                return dfs(i + 1, j, s - nums[i]) or dfs(i, j - 1, s - nums[j])
            


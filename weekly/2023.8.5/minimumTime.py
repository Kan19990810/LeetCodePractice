class Solution:
    def minimumTime(self, nums1: List[int], nums2: List[int], x: int) -> int:
        # 每秒增加sum(nums2)
        # 贪心 归0 肯定归最大值
        
        # 如何维护最大值
        #  还要更新每个值
        current = sum(nums1)
        addition = sum(nums2)
        n = len(nums1)
        nums = []
        ans = 0
        for i in range(n):
            nums.append([nums1[i], i])

        nums.sort(key= lambda x: -x[0])

        while(nums[0][0] + nums2[nums[0][1]] > addition):
            current += addition - nums[0][0] + nums2[nums[0][1]]
            ans += 1
            if current <= x:
                return ans
            
            for i in range(n):
                nums[i][0] += nums2[nums[i][1]]
                
            nums.sort(key= lambda x: -x[0])

        return -1



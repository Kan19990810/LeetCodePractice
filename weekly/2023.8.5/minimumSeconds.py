class Solution:
    def minimumSeconds(self, nums: List[int]) -> int:
        # 相当于是变成相邻的数或者不变
        # 10 ^ 5 次方 说明没办法暴力  n log n
        # nums[i] 变为 nums[j] 需要 min(abs(j - i), abs(j - i + n), abs(i - j + n)) 次
        # 有没有办法只需要知道相同数的坐标位置即可
        # [0 ~ 3] [0, 2] 
        num_unique = []
        unique_index = {}
        n = len(nums)
        k = 0
        for i in range(n):
            # 如果没有记录该数字，给该数字分配一行
            if nums[i] not in unique_index:
                unique_index[nums[i]] = k
                num_unique.append([i])
                k += 1
                
            else:
                # 在该数字的行中添加该数字的下标
                num_unique[unique_index[nums[i]]].append(i)
            # print(unique_index, num_unique)
        ans = inf
        for index in num_unique:
            m = len(index)
            res = 0
            # all wrong
            # 已知相邻坐标 i, j (0, 1) (0, 2) (0, 3)则 mid = i + j >> 1
            # 中间有i - j - 1  (1 + ... + k) * 2 or (1 + ... + k - 1) * 2 + k
            #  mid = (i - j - 1) // 2 diff = (i - j - 1) % 2
            #   diff == 0 为 res = (1 + mid) * mid // 2 
            #   diff == 1 res = mid + 1 + (mid + 1) * mid // 2 (0, 2) mid = 0 (0, 4) = 1
            #  [0, 4]  1 2 3  diff = 1 mid = 1 (1 + .. + mid ) +(mid + 1) 
            # [0, 5]  1 2 3 4
            for i in range(m - 1):
                x, y = index[i], index[i + 1]
                mid = (y - x) // 2
                res = max(res, mid)
            # 考虑循环情况 x = index[0] , y = index[m - 1] - n
            x, y = index[0], index[m - 1] - n
            mid = (x - y) // 2
            res = max(res, mid)
            ans = min(ans, res)
        return ans

        

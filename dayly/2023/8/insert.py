class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # res = []
        # # 逐个扫描interval
        # st, ed = -1, -1
        # bo = False
        # for interval in intervals:

        #     # 如果新左端点大于待定右端点，待定区间确定
        #     if ed < interval[0]:
        #         if ed != -1:
        #             res.append([st, ed])
        #         st, ed = interval[0], interval[1]

        #     # 合并
        #     else:
        #         st, ed = min(st, interval[0]), max(ed, interval[1])
            
            
        #     if not bo and st > newInterval[1]:
        #         res.append(newInterval)
        #         bo = True
        #     # 判断待定区间适合和NEW有交集
        #     if not bo and st <= newInterval[0] <= ed or st <= newInterval[1] <= ed or newInterval[0] <= st <= newInterval[1] or newInterval[0] <= ed <= newInterval[1]:
        #         st, ed = min(st, newInterval[0]), max(ed, newInterval[1])
        #         bo = True

        # if ed != -1:
        #     res.append([st, ed])
        # if not bo:
        #     res.append(newInterval)
        # return res

        l , r = newInterval
        placed = False

        ans = []

        for li, ri in intervals:
            if li > r:
                if not placed:
                    ans.append([l, r])
                    placed = True
                ans.append([li, ri])

            elif ri < l:
                ans.append([li, ri])

            else:
                left = min(l, li)
                r= max(r, ri)
        if not placed:
            ans.append([l, r])
        return ans
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        merged = []

        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged
        
        # i, n = 0, len(intervals)
        # intervals.sort()
        # print(intervals)
        # ans = []
        # res = [intervals[0][0], intervals[i][1]]

        # while i < n:
        #     ma = res[1]
        #     l, r = i, n - 1
        #     while l < r:
        #         mid = (l + r + 1) >> 1
        #         if intervals[mid][0] <= ma:
        #             l = mid
        #         else:
        #             r = mid - 1
        #     if l == i:
        #         ans.append(res)
        #         i = l + 1
        #         if i < n:
        #             res = [intervals[i][0], intervals[i][1]]

        #     else:
        #         res[1] = max(res[1], max(intervals[a][1] for a in range(i, l + 1)))
        #         i = l
        # return ans
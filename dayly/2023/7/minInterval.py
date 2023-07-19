class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # queries 递增的下标
        qindex = list(range(len(queries)))
        qindex.sort(key=lambda i: queries[i])
        # 按intervals 左端点进行排序
        intervals.sort(key=lambda i: i[0])
        pq = []
        res = [-1] * len(queries)
        i = 0
        for qi in qindex:
            while i < len(intervals) and intervals[i][0] <= queries[qi]:
                # 最小堆， 最前的是长度最小的
                heappush(pq, (intervals[i][1] - intervals[i][0] + 1, intervals[i][0], intervals[i][1]))
                i += 1
            # 排除右端点不符合要求的
            while pq and pq[0][2] < queries[qi]:
                heappop(pq)
            if pq:
                res[qi] = pq[0][0]
        return res

import heapq
from typing import List
class Solution:
    def findCrossingTime(self, n: int, k: int, time: List[List[int]]) -> int:
        time.sort(key=lambda x: x[0] + x[2])
        cur = 0
        wait_in_left, wait_in_right = [], []
        work_in_left, work_in_right = [], []
        for i in range(k):
            # 初始所有工人在左岸排队
            heapq.heappush(wait_in_left, -i)
        while 1:
            # 左右岸搬东西可以同时进行
            # 当前时间内左岸搬完东西的人回到左岸等待过岸
            while work_in_left:
                # TODO work_in_left[0] 含有2 个数？
                t, i = work_in_left[0]
                if t > cur:
                    break
                heapq.heappop(work_in_left)
                heapq.heappush(wait_in_left, -i)
            # 当前时间内右岸办完东西的人回到右岸等待过岸
            while work_in_right:
                t, i = work_in_right[0]
                if t > cur:
                    break
                heapq.heappop(work_in_right)
                heapq.heappush(wait_in_right, - i)
            # 左岸去右岸的条件：还有货物没搬完且左岸有人等待
            left_to_go = n > 0 and wait_in_left
            # 右岸去左岸的条件：右岸有人等待
            right_to_go = bool(wait_in_right)
            # 当左右岸都没人想过河时更新时刻到最近的完成工作的时刻
            if not left_to_go and not right_to_go:
                nxt = inf
                if work_in_left:
                    nxt = min(nxt,work_in_left[0][0])
                if work_in_right:
                    nxt = min(nxt, work_in_right[0][0])
                cur = nxt
                continue
            # 右岸过岸优先度更高
            if right_to_go:
                # 右岸等待优先度最高的人过河，更新时刻到过岸后的时间
                i = -heapq.heappop(wait_in_right)
                cur += time[i][2]
                # 最后一个搬箱子的到达左岸时返回答案
                if n == 0 and not wait_in_right and not work_in_right:
                    return cur
                # 到达右岸后，立刻进入左岸工作
                heapq.heappush(work_in_left, (cur + time[i][3], i))
            else:
                # 到达左岸后更新时间，并立刻进行工作
                i = -heapq.heappop(wait_in_left)
                cur += time[i][0]
                n -= 1
                heapq.heappush(work_in_right, (cur + time[i][1], i))
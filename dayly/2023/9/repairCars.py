import heapq
import math
class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        # 维护一个单调队列  
        
        # n, m = len(ranks), cars    
        # O(mnlogn)?
        
        # heap = []
        # n = len(ranks)
        # for i in range(n):
        #     heapq.heappush(heap,[ranks[i], ranks[i], 1])

        # ans = 0
        # for i in range(cars):
        #     r = heapq.heappop(heap)
        #     ans = r[0]
        #     heapq.heappush(heap, [r[1] * (r[2] + 1) * (r[2] + 1), r[1], r[2] + 1])

        # return ans
        

        # 二分查找

        # O(nlogm)?

        n = len(ranks)
        ranks.sort()

        l, r = 0, ranks[0] * cars * cars

        while l < r:
            mid = (l + r) >> 1

            if (self.valid(mid, ranks, cars)): r = mid 
            else: l = mid + 1

        return r

    def valid(self, x: int, ranks: List[int], cars: int) -> bool:
        res = 0
        for i in ranks:
            res += int(math.sqrt(x // i))

        return res >= cars


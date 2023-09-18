class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        
        courses.sort(key = lambda c: c[1])

        q = list()

        total = 0

        for ti, di in courses:
            if total + ti <= di:
                total += ti
                # 大根堆
                heapq.heappush(q, -ti)

            elif q and -q[0] > ti:
                total -= -q[0] - ti
                heapq.heappop(q)
                heapq.heappush(q, - ti)

        return len(q)
        # now = 0
        # ans = 0
        # res = 0
        # n = len(courses)
        # achieve = [0] * n

        # def dfs(i):

        #     nonlocal now, ans, res

        #     # 已经学过了
        #     if achieve[i] == 1:
        #         return
            
        #     # 时间不够
        #     if now + courses[i][0] > courses[i][1]:
        #         return
            
        #     # 开始学
        #     achieve[i] = 1
        #     now += courses[i][0]
        #     res += 1
        #     ans = max(ans, res)

        #     # 学下一门
        #     for i in range(n):
        #         dfs(i)

        #     # 回溯一下
        #     achieve[i] = 0
        #     res -= 1

        # dfs(0)
        # return ans



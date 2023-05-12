from collections import Counter


class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        builds = Counter(range(n))
        # print(builds)
        requestsLen = len(requests)
        ans, num = 0, 0

        def dfs(i):
            nonlocal ans, num
            if i == requestsLen:
                if all(builds[idx] == 1 for idx in range(n)):
                    ans = max(ans, num)
                return

            dfs(i + 1)

            builds[requests[i][0]] -= 1
            builds[requests[i][1]] += 1
            num += 1

            dfs(i + 1)

            builds[requests[i][0]] += 1
            builds[requests[i][1]] -= 1
            num -= 1

        dfs(0)
        return ans



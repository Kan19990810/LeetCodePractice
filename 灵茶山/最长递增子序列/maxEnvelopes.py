class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        n = len(envelopes)
        g = []
        for i in range(n):
            left, right = 0, len(g) - 1
            while left <= right:
                mid = (left + right) // 2
                if envelopes[i][1] > g[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
            if left == len(g):
                g.append(envelopes[i][1])
            else:
                g[left] = envelopes[i][1]
        return len(g)
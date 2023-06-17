from collections import Counter
class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:

        n = len(s)
        count = [0] * (n + 1)
        for i in range(n):
            count[i + 1] = count[i] ^ (1 << (ord(s[i]) - ord('a')))
        res = []
        for l, r, k in queries:
            bits = (count[r + 1] ^ count[l]).bit_count()
            res.append(bits <= k * 2 + 1)
        return res



        # ans = []
        # c = Counter()
        # n = len(s)
        # pre = [0] * (n + 1)
        # for i, num in enumerate(s):
        #     c[num] += 1
        #     if c[num] % 2 == 1:
        #         pre[i + 1] = pre[i] + 1
        #     else:
        #         pre[i + 1] = pre[i] - 1
        #
        # for query in queries:
        #     if abs(pre[query[1] + 1] - pre[query[0]]) // 2 < query[2]:
        #         ans.append(True)
        #     else:
        #         ans.append(False)
        # return ans





        # for query in queries:
        #     st = Counter(s[query[0]:query[1] + 1])
        #     c = 0
        #     for key in st:
        #         if st[key] % 2 != 0:
        #             c += 1
        #
        #     if (c // 2) <= query[2]:
        #         ans.append(True)
        #     else:
        #         ans.append(False)
        #
        # return ans

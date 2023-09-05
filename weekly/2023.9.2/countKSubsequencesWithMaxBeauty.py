from collections import Counter
class Solution:
    def countKSubsequencesWithMaxBeauty(self, s: str, k: int) -> int:
        num_count = Counter(s)

        count_sort = []

        for x in num_count:
            count_sort.append(num_count[x])

        if k > len(count_sort):
            return 0


        count_sort.sort(reverse=True)
        # print(count_sort)
        ans = 1
        mod = 10**9 + 7
        pre = -1
        c = 0
        for i in range(k):
            if count_sort[i] != count_sort[k - 1]:
                ans *= count_sort[i]
                ans %= mod
            else:
                c += 1
            # print(ans)
        time = 0
        for i in range(k, len(count_sort)):
            # print(count_sort[i], count_sort[k - 1])
            if count_sort[i] == count_sort[k - 1]:
                
                time += 1
        # 最小的哪个数有几个 c (c)(c + time) * count_sort[k - 1] ** c
        a = 1
        for i in range(time + 1, c + time + 1):
            a *= i
        for i in range(1, c + 1):
            a //= i

        ans += a * (count_sort[k - 1] ** c)
        ans %= mod
        return ans
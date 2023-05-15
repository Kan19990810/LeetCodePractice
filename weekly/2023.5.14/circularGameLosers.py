from collections import Counter
class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:

        count = Counter()
        ans = []

        idx, time = 0, 0

        while idx not in count:
            count[idx] += 1
            time += 1
            idx = (idx + time * k) % n

        for i in range(n):
            if i not in count:
                ans.append(i + 1)

        return ans


from collections import Counter
class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        # n = 10^5 nlogn
        # 偶数差下标可以互换计数即可
        n = len(s1)
        s1_one = Counter()
        s1_two = Counter()
        s2_one = Counter()
        s2_two = Counter()

        for i in range(n):
            if i % 2 == 0:
                s1_one[s1[i]] += 1
                s2_one[s2[i]] += 1
            else:
                s1_two[s1[i]] += 1
                s2_two[s2[i]] += 1

        return s1_one == s2_one and s1_two == s2_two
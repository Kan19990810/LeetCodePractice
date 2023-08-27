class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        s = set()

        idx = 0
        i = 1
        while(idx not in s):
            s.add(idx)

            idx = idx + i * k
            idx %= n
            i += 1
        
        ans = []
        for i in range(n):
            if i not in s:
                ans.append(i + 1)

        return ans
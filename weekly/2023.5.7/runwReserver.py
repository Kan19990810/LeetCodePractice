class Solution:
    def runeReserve(self, runes: List[int]) -> int:
        runes.sort()
        n = len(runes)
        idx, cur, ans = 1, 1, 1

        while idx < n:
            if runes[idx] - runes[idx - 1] <= 1:
                cur += 1
                ans = max(cur, ans)

            else:
                cur = 1

            idx += 1

        return ans

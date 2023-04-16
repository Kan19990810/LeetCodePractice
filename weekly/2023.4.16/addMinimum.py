class Solution:
    def addMinimum(self, word: str) -> int:
        n = len(word)
        idx = 0
        ans = 0

        while idx < n:

            while idx < n and word[idx] != 'a':
                if idx == n - 1:
                    idx += 1
                    ans += 2
                    continue
                if idx < n - 1 and word[idx] == 'b' and word[idx + 1] == 'c':
                    idx += 2
                    ans += 1
                    continue
                if idx < n - 1 and word[idx] == 'b' and word[idx + 1] != 'c':
                    idx += 1
                    ans += 2
                    continue
                if idx < n - 1 and word[idx] == 'c':
                    idx += 1
                    ans += 2
                    continue
            if idx == n - 2 and word[idx + 1] != 'a':
                idx += 2
                ans += 1
                continue
            if idx == n - 2 and word[idx + 1] == 'a':
                idx += 2
                ans += 4
                continue
            if idx == n - 1:
                idx += 1
                ans += 2
                continue

            if idx < n - 2 and word[idx + 1] == 'b' and word[idx + 2] == 'c':
                idx += 3
                continue
            if idx < n - 2 and word[idx + 1] == 'b' and word[idx + 2] != 'c':
                idx += 2
                ans += 1
                continue
            if idx < n - 2 and word[idx + 1] == 'c':
                idx += 2
                ans += 1
                continue
            if idx < n - 2 and word[idx + 1] == 'a':
                idx += 1
                ans += 2
                continue

        return ans

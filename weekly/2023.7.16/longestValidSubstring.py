class Solution:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        n = len(word)

        left, right = 0, n
        while right >= left:
            mid = (left + right) // 2
            if self.bo(word, mid, n, forbidden):
                left = mid + 1
            else:
                right = mid - 1
            print(left, right, mid)
        return right

    def bo(self, word: str, mid: int, n: int, forbidden: List[str]) -> bool:
        for i in range(n - mid + 1):
            s = word[i : i + mid]
            print(s, self.isNotIn(s, forbidden))
            if self.isNotIn(s, forbidden):
                return True
        return False

    def isNotIn(self, s: str, forbidden: List[str]) -> bool:
        for i in forbidden:
            if i in s:
                return False

        return True

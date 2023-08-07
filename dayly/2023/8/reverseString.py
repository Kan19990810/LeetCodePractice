class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        first, second = 0, n - 1
        while (first < second):
            cmt = s[second]
            s[second] = s[first]
            s[first] = cmt
            first += 1
            second -= 1

        return s  
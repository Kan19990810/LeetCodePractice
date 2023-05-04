class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        left, right = 0, 0
        n = len(fruits)
        s = 0
        ans = 0

        def step(left: int, right: int) -> int:
            if fruits[right][0] <= startPos:
                return startPos - fruits[left][0]
            elif fruits[left][0] >= startPos:
                return fruits[right][0] - startPos
            else:
                return min(abs(startPos - fruits[right][0]), abs(startPos - fruits[left][0])) + fruits[right][0] - fruits[left][0]

        while right < n:
            s += fruits[right][1]
            while left <= right and step(left, right) > k:
                s -= fruits[left][1]
                left += 1

            ans = max(ans, s)
            right += 1
        return ans

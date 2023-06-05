class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        n = len(price)
        price.sort()
        if n == 1:
             return 0
        if n == 2:
             return price[-1] - price[0]

        left, right = 0, (price[-1] - price[0]) // (k - 1)
        while left <= right:
            mid = (left + right) // 2
            pre, count = price[0], 1
            for i in range(1, n):
                if price[i] - pre >= mid:
                    pre = price[i]
                    count += 1
            if count >= k:
                left = mid + 1
            else:
                right = mid - 1
        return left - 1

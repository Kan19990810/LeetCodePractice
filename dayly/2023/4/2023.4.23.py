class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        n = len(books)
        dp = [1000000] * (n + 1)
        dp[0] = 0
        for i, b in enumerate(books):
            curWidth = 0
            maxHeight = 0
            j = i
            while j > 0:
                curWidth += books[j][0]
                if curWidth > shelfWidth:
                    break
                maxHeight = max(maxHeight, books[j][1])
                dp[i + 1] = min(dp[i + 1], dp[j] + maxHeight)
                j -= 1
        return dp[n]
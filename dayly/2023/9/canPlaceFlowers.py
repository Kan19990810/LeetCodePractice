class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        ans = 0
        m = len(flowerbed)
        i, j = 0, 0

        while j < m and flowerbed[j] == 0:
            j += 1
        
        if j == m:
            ans += (j - i + 1) // 2

        else:
            ans += (j - i) // 2

        j += 1
        i = j

        while (j < m):
            if flowerbed[j] == 0:
                j += 1

            else:
                if j - i > 1:
                    ans += (j - i - 1) // 2
                j += 1
                i = j

        
        ans += (j - i) // 2
        
        return True if ans == n else False


        


                
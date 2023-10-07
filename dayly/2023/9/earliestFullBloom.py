class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        def compare_fn(i: int, j: int) -> int:
            if growTime[i] > growTime[j]:
                return -1

            if growTime[i] < growTime[j]:
                return 1

            return 0

        n = len(plantTime)
        idx = list(range(n))
        idx.sort(key=cmp_to_key(compare_fn))

        prev = ans = 0
        for i in idx:
            ans = max(ans, prev + plantTime[i] +growTime[i])
            prev += plantTime[i]
        
        return ans
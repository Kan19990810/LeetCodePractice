import collections
class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        # 差分 + 离散化 + 双指针
        cnt = collections.defaultdict(int)
        for start, end in flowers:
            cnt[start] += 1
            cnt[end + 1] -= 1
        
        arr = sorted(cnt.items())
        m = len(people)

        ans = [0] * m
        j, curr = 0, 0

        for p, i in sorted(zip(people, range(m))):
            while j < len(arr) and arr[j][0] <= p:
                curr += arr[j][1]
                j += 1
            ans[i] = curr
        return ans

        

        


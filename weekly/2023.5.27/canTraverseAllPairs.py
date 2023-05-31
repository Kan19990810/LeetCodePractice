from math import sqrt
class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        def findEle(num):
            se = set()
            for i in range(2, int(sqrt(num))):
                if num % i == 0:
                    se.add(i)
                    while num % i == 0:
                        num //= i
            return se

        su = findEle(nums[0])
        bo = True
        re = []
        while bo:
            bo, po = False, False
            se = findEle(nums[0])
            re = []
            for i in nums:
                se1 = findEle(i)
                for j in se1:
                    if j in se:
                        se.update(se1)
                        po = True
                        break
                re.append(i)
            if po:
                nums = re
                for j in se:
                    if j in su:
                        su.update(se)
                        bo = True
                        break







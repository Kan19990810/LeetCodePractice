class Solution:
    def addNegabinary(self, arr1: List[int], arr2: List[int]) -> List[int]:
        result = []
        n1, n2 = len(arr1), len(arr2)
        sum1, sum2, sum3 = 0, 0, 0
        for i in arr1:
            n1 -= 1
            sum1 += i * ((-2) ** n1)
        for i in arr2:
            n2 -= 1
            sum2 += i * ((-2) ** n2)
        sum3 = sum1 + sum2
        while sum3 != 0:
            if sum3 % 2 == 0:
                result.append(0)
                sum3 //= -2
            if sum3 % 2 == -1:
                result.append(1)
                sum3 //= -2
                sum3 += 1
        return result[::-1]

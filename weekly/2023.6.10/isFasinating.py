
class Solution:
    def isFascinating(self, n: int) -> bool:
        count = set()
        for i in range(3):
            num = n * (n + 1)
            while num > 0:
                ele = num % 10
                num //= 10
                if ele == 0 or ele in count:
                    return False
                else:
                    count.add(ele)
        return True

from collections import Counter
class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        """
        dic={'偶数‘： 次数}
        :param nums:
        :return:
        """
        dic = Counter()
        ma = 0
        res = -1
        for _, num in enumerate(nums):
            if num % 2 == 0:
                dic[num] += 1
                if dic[num] == ma:
                    res = min(res, num)
                elif dic[num] >= ma:
                    res = num
                    ma = dic[num]
        print(dic)
        return res
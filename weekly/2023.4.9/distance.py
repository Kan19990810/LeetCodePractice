class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        """
        还是应该用dict
        :param nums:
        :return:
        """
        n = len(nums)
        res = [0] * n
        dic = {}
        store = [[]]
        dis = [[]]
        va = 0

        for i in range(n):
            if nums[i] not in dic:
                dic[nums[i]] = va
                va += 1
                dis.append([])
                dis[dic[nums[i]]].append(0)
                store.append([])
                store[dic[nums[i]]].append(i)
            else:
                dis[dic[nums[i]]].append(i - store[dic[nums[i]]][-1])
                store[dic[nums[i]]].append(i)
            #print(dic[nums[i]])

            #print(store[dic[nums[i]]])

        for i in range(n):
            m = len(dis[dic[nums[i]]])
            if m == 1:







                res[i] = 0
            else:

            for j in range(m):
                if i != store[dic[nums[i]]][j]:
                    res[i] += abs(i - store[dic[nums[i]]][j])
            #print(res[i])
        #print(dic, va)
        #print(store)
        return res

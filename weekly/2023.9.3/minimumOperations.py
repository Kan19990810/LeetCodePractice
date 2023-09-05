class Solution:
    def minimumOperations(self, num: str) -> int:
        # 判断最后两位数

        n = len(num)
        ans = n
        index_00 = -1
        index_01 = -1
        index_2  = -1
        index_5  = -1
        index_7  = -1
        # 后缀 00 ， 25， 50 ， 75
        for i in range(n - 1, - 1, -1):
            if num[i] == '0':
                if index_00 == -1:
                    index_00 = i
                else:
                    index_01 = max(index_01, i)
            
            if num[i] == '5':
                index_5 = max(index_5, i)
            
            if num[i] == '2' and i < index_5:
                index_2 = max(index_2, i)

            if num[i] == '7' and i < index_5:
                index_7 = max(index_7, i)
        if index_00 != -1:
            ans = min(ans, n - 1)

        if index_01 != -1:
            ans = min(ans, n - index_01 - 2)

        if index_2 != -1:
            ans = min(ans, n - index_2 - 2)
        
        if index_5 != -1 and index_00 > index_5:
            ans = min(ans, n - index_5 - 2)
        
        if index_7 != -1:
            ans = min(ans, n - index_7 - 2)
        print(index_01, index_00, index_2, index_5, index_7)
        return ans
        


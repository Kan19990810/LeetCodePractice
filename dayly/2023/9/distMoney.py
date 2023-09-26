class Solution:
    def distMoney(self, money: int, children: int) -> int:
        left = money - children
        if left < 0:
            return -1
        
        res = left // 7
        left %= 7

        if res == children - 1 and left == 3:
            return res - 1
        
        
        if res == children and left > 0:
            return res - 1
        
        if res > children:
            return children - 1

        return res 
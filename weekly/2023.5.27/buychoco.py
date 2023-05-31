class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        su = prices[0] + prices[1]
        return money - su if money >= su else money


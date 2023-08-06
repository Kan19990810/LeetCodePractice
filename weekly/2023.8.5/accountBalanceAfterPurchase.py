class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        i = purchaseAmount % 10
        j = purchaseAmount // 10
        if i >= 5:
            cost = (j + 1) * 10

        else:
            cost = j * 10

        return 100 - cost
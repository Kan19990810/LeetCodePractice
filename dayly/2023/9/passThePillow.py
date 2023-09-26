class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        if ((time - 1) // (n - 1)) % (n - 1) == 0:
            return (time - 1) % (n - 1) + (n - 1)
        else:
            return (n - 1) - (time - 1) % (n - 1)
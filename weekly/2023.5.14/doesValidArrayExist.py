class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        n = len(derived)

        # original[0] = 0
        original = [0] * n
        for i in range(1, n):
            original[i] = original[i - 1] ^ derived[i - 1]

        if derived[n - 1] == original[n - 1] ^ original[0]:
            return True

        # original[0] = 1

        original = [0] * n
        original[0] = 1

        for i in range(1, n):
            original[i] = original[i - 1] ^ derived[i - 1]

        if derived[n - 1] == original[n - 1] ^ original[0]:
            return True

        return False



class Solution:
    def punishmentNumber(self, n: int) -> int:
        ans = 0

        def isPunish(idx, left):
            if left < 0:
                return False

            if idx == len(po):
                if left == 0:
                    return True
                return False

            for i in range(idx, len(po)):
                if isPunish(i + 1, left - int(po[idx: i + 1])):
                    return True

            return False

        for num in range(1, n + 1):
            po = str(num * num)
            if isPunish(0, num):
                print(num)
                ans += num * num
        return ans







class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        f, second = 0, n - 1
        while f < second:
            if numbers[f] + numbers[second] == target:
                return [f + 1, second + 1]
            elif numbers[f] + numbers[second] < target:
                f += 1
            else:
                second -= 1

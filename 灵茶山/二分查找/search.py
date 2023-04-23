class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)

        left = 0
        right = n - 1
        print(left, right)

        while right >= left:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid

            if nums[mid] > target:
                if nums[left] > nums[mid] < nums[right]:
                    right = mid - 1
                    continue
                if nums[left] > target:
                    left = mid + 1
                else:
                    right = mid - 1

            else:
                if nums[left] < nums[mid] > nums[right]:
                    left = mid + 1
                    continue
                if nums[right] < target:
                    right = mid - 1
                else:
                    left = mid + 1

            print(left, mid, right)

        return right if nums[right] == target else -1

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = -1, len(nums) -1
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] < nums[-1]:
                right = mid
            else:
                left = mid
        return right

    def lower_bound(self, nums:List[int], left: int, right: int, target: int) -> int:
        r = right
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid
            else:
                right = mid
        return right if right < r and nums[right] == target else -1

    def search(self, nums: List[int], target: int) -> int:
        i = self.findMin(nums)
        if target > nums[-1]:
            left, right = -1, i
        else:
            left, right = i - 1, len(nums)
        return self.lower_bound(nums, left, right, target)

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def findMin(nums: List[int]) -> int:
            l = 0
            r = len(nums)
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] > nums[-1]:
                    l = mid + 1
                else:
                    r = mid - 1
            return r + 1
        if target > nums[-1]:
            left = 0
            right = findMin(nums) - 1
        else:
            left = findMin(nums)
            right = len(nums)
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid +1
            else:
                right = mid - 1
        return right + 1 if nums[right + 1] == target else -1

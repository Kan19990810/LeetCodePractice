class Solution:
    def search(self, nums: List[int], target: int) -> int:
        = len(nums)

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

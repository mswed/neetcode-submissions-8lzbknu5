class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left = 0
        right = len(nums) - 1
        while left <= right:
            middle = (right + left) // 2
            found = nums[middle]
            if found == target:
                return middle
            if found > target:
                right = middle - 1
            if found < target:
                left = middle + 1

        return -1

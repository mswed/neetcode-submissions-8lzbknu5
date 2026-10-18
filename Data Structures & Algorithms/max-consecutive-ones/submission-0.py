class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_found = 0
        current_streak = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                current_streak += 1
            else:
                current_streak = 0

            max_found = max(max_found, current_streak)

        return max_found

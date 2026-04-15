class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        difference = {}

        for i, n in enumerate(nums):
            if n in difference:
                return [difference[n], i]

            difference[target - n] = i

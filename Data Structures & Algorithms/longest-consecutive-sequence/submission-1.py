class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        start_check = set(nums)

        runs = {}

        # Build a list of start indexes
        for s in range(len(nums)):
            # start with just one number
            starting_index = s
            starting_value = nums[starting_index]

            if starting_value - 1 not in start_check:
                runs[starting_index] = 1

        for s in runs.keys():
            value = nums[s]
            current = value
            while current + 1 in start_check:
                runs[s] += 1
                current += 1

        if not nums:
            return 0

        return max(list(runs.values()))

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []

        nums.sort()
        for n in range(len(nums)):
            # We skip duplicate values (notice we're also skipping 0 so our math doesn't throw us to the end of the list)
            if n > 0 and nums[n] == nums[n - 1]:
                continue
            target = 0 - nums[n]

            start = n + 1
            end = len(nums) - 1

            while start < end:
                r = nums[start] + nums[end]
                if r == target:
                    # We found a match
                    res.append([nums[n], nums[start], nums[end]])
                    # Go to the next start index
                    start += 1
                    # Now skip duplicates for start and end
                    while start < end and nums[start] == nums[start - 1]:
                        start += 1
                    while (
                        start < end
                        and end + 1 < len(nums)
                        and nums[end] == nums[end + 1]
                    ):
                        end -= 1

                elif r > target:
                    end -= 1
                elif r < target:
                    start += 1

        return res

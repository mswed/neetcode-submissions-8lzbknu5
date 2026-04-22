class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = {}

        nums.sort()
        for n in range(len(nums)):
            target = 0 - nums[n]

            start = n + 1
            end = len(nums) - 1

            while start < end:
                r = nums[start] + nums[end]
                if r == target:
                    base = str(sorted([nums[n], nums[start], nums[end]]))
                    key = "".join(base)
                    res[key] = [nums[n], nums[start], nums[end]]
                    start += 1

                if r > target:
                    end -= 1
                if r < target:
                    start += 1

        return list(res.values())

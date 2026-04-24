class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        steps = len(nums) - k
        max_values = []
        l = 0
        r = k - 1
        for s in range(steps + 1):
            res = nums[l : r + 1]
            max_values.append(max(res))
            l += 1
            r += 1

        print(max_values)
        return max_values

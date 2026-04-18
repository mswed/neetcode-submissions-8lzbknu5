class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        prefix = [1] * length
        suffix = [1] * length
        res = [1] * length

        # Calc prefix
        for i in range(1, length):
            prefix[i] = nums[i - 1] * prefix[i - 1]

        # Calc suffix
        for i in range(length - 2, -1, -1):
            suffix[i] = nums[i + 1] * suffix[i + 1]

        # Calc results
        for i in range(0, length):
            res[i] = prefix[i] * suffix[i]

        return res


s = Solution()
s.productExceptSelf([1, 2, 4, 6])

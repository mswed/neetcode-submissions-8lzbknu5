class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mapping = {}
        for n in nums:
            if n in mapping:
                mapping[n] += 1
                if mapping[n] > 1:
                    return True
            else:
                mapping[n] = 1

        return False

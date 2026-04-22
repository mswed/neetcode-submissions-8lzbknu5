class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        end = len(numbers) - 1

        while start < end:
            res = numbers[start] + numbers[end]
            if res == target:
                return [start + 1, end + 1]
            if res > target:
                end -= 1
            if res < target:
                start += 1

        return [-1, -1]

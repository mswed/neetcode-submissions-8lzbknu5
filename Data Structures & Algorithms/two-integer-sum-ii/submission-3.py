class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            first = i
            second = i + 1

            while second < len(numbers):
                if second > len(numbers):
                    continue
                if numbers[first] + numbers[second] == target:
                    return [first + 1, second + 1]

                second += 1

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        new_arr = [0 for i in range(len(arr))]
        for i in range(len(arr) - 1, -1, -1):
            if i + 1 >= len(arr):
                new_arr[i] = -1
            else:
                new_arr[i] = max(arr[i + 1], new_arr[i + 1])

        return new_arr

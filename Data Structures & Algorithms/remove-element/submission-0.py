class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Naive solution
        count = 0
        i = 0
        while i < len(nums):
            if nums[i] == val:
                self.remove(nums, i)
                i -= 1
                count -= 1
            else:
                count += 1

            i += 1

        return count

    def remove(self, arr, target):
        # Shift starting one item to the right of target
        for i in range(target + 1, len(arr)):
            arr[i - 1] = arr[i]

        # The last item is now gone so...
        arr[-1] = "_"

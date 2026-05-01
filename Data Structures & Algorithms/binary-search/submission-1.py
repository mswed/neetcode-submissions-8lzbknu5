class Solution:
    def search(self, nums: List[int], target: int) -> int:

        search_list = nums
        start_index = 0
        while search_list:
            middle = len(search_list) // 2
            found = search_list[middle]
            if found == target:
                return start_index + middle
            if found > target:
                search_list = search_list[:middle]
            if found < target:
                search_list = search_list[middle + 1 :]
                start_index = start_index + middle + 1

        return -1

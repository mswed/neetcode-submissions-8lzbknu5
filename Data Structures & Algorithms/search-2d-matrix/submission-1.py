from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0
        bottom = len(matrix) - 1
        while top <= bottom:
            middle = (top + bottom) // 2
            row_end = matrix[middle][-1]
            row_start = matrix[middle][0]
            if row_start > target:
                # The start of the row is still too large we need to go back
                bottom = middle - 1

            elif row_end < target:
                # The target can be on the next rows
                top = middle + 1

            else:
                # The target might be on this row (or not at all)
                left = 0
                right = len(matrix[middle]) - 1
                while left <= right:
                    r_middle = (left + right) // 2
                    if matrix[middle][r_middle] == target:
                        # we found the target in the row
                        return True
                    if matrix[middle][r_middle] > target:
                        # search back
                        right = r_middle - 1
                    if matrix[middle][r_middle] < target:
                        # search forward
                        left = r_middle + 1

                # We searched the row and found nothing
                return False

        return False

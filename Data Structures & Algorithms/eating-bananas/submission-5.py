from typing import List
import math


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # binary search solution
        left = 1
        right = max(piles)
        min_found = max(piles)

        while left <= right:
            middle = (left + right) // 2
            time_left = h
            for p in piles:
                time_left = time_left - math.ceil(p / middle)

            if time_left >= 0:
                right = middle - 1
                min_found = min(min_found, middle)
            if time_left < 0:
                left = middle + 1

        return min_found

from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Naive solution
        print(heights)
        areas = []
        for bar in range(len(heights)):
            h1 = heights[bar]
            # The bar itself can be a valid ractangle
            areas.append(h1)
            current_min = h1
            for nb in range(bar + 1, len(heights)):
                h2 = heights[nb]
                current_min = min(current_min, h2)
                width = nb - bar + 1
                area = min(h1, h2, current_min) * width
                areas.append(area)

        return max(areas)

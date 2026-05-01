from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        print(heights)
        max_area = 0
        stack = []
        for i, h in enumerate(heights):
            if not stack:
                stack.append((h, i))
            elif h < stack[-1][0]:
                # this is the right limit so
                left_limit_index = stack[-1][1]
                while stack and h < stack[-1][0]:
                    # As long as we can go back...
                    # Pop the top
                    h1, index = stack.pop()
                    width = i - index
                    area = h1 * width
                    max_area = max(area, max_area)
                    left_limit_index = index
                # Now we add the new bar but set the index to the old top
                # to mark that we can expand left up to that point
                stack.append((h, left_limit_index))
            else:
                stack.append((h, i))

        if stack:
            # We have leftovers
            while stack:
                h1, index = stack.pop()
                width = len(heights) - index
                area = h1 * width
                max_area = max(area, max_area)

        return max_area

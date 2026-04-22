class Solution:
    def maxArea(self, heights: List[int]) -> int:
        areas = []
        left = 0
        right = len(heights) - 1
        while left < right:
            bottom = right - left
            area = bottom * min(heights[left], heights[right])
            areas.append(area)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return max(areas)

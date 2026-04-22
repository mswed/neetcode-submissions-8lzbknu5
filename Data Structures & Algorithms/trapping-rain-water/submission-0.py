class Solution:
    def trap(self, height: List[int]) -> int:
        res = []
        for bar in range(len(height)):
            left = bar - 1 if bar > 0 else 0
            right = bar + 1 if bar + 1 < len(height) else len(height) - 1
            max_right = 0
            max_left = 0

            while left >= 0:
                max_left = max(max_left, height[left])
                left -= 1

            while right < len(height):
                max_right = max(max_right, height[right])
                right += 1

            water = max(0, min(max_left, max_right) - height[bar])
            res.append(water)

        return sum(res)

class Solution:
    def trap(self, height: List[int]) -> int:
        prefix = [0 for _ in range(len(height))]
        suffix = [0 for _ in range(len(height))]
        res = []

        # Calculate prefix
        max_value = 0
        for p in range(len(height)):
            left = height[p - 1] if p > 0 else 0
            max_value = max(left, max_value)
            prefix[p] = max_value

        # Calculate suffix
        max_value = 0
        for s in range(len(height) - 2, -1, -1):
            right = height[s + 1]
            max_value = max(right, max_value)
            suffix[s] = max_value

        for bar in range(len(height)):
            max_left = prefix[bar]
            max_right = suffix[bar]

            water = max(0, min(max_left, max_right) - height[bar])
            res.append(water)

        return sum(res)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        suffix = [0] * len(prices)
        difference = [0] * len(prices)
        max_price = 0
        for p in range(len(prices) - 2, -1, -1):
            right = prices[p + 1]
            max_price = max(max_price, right)
            suffix[p] = max_price

        for d in range(len(prices)):
            diff = suffix[d] - prices[d]
            difference[d] = diff

        return max(difference) if max(difference) > 0 else 0

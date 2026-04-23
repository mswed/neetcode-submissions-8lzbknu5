class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buy_day = 0
        sell_day = 1

        while sell_day < len(prices):
            buy_price = prices[buy_day]
            sell_price = prices[sell_day]
            max_profit = max(max_profit, sell_price - buy_price)

            if buy_price > sell_price:
                # We need a cheaper buy price
                buy_day += 1
                sell_day = buy_day + 1

            elif buy_price <= sell_price:
                # We have a good buy price move search for a good sell price
                sell_day += 1

        return max_profit

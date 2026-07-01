class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) < 2:
            return 0

        max_profit = 0
        min_price = prices[0]

        for curr_price in prices:
            max_profit = max(max_profit, curr_price - min_price)

            # Update min price for future references
            min_price = min(min_price, curr_price)


        return max_profit
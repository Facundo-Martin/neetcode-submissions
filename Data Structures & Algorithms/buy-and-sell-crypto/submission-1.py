class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        max_profit = 0
        min_price = 0

        for i in range(n):
            curr_price = prices[i]
            min_price = min(min_price, curr_price)

            max_profit = max(max_profit, prices[i] - min_price)

        return max_profit
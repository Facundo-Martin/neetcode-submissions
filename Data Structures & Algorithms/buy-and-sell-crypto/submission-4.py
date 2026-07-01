class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        max_profit = 0
        min_price = prices[0]

        for i in range(n):
            curr_price = prices[i]
            max_profit = max(max_profit, curr_price - min_price)

            min_price = min(min_price, curr_price)


        return max_profit
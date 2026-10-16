class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        max_profit = 0

        for i in range(1, len(prices)):
            profit = prices[i] - buy
            if prices[i] < buy:
                buy = prices[i]
            if profit > max_profit: max_profit = profit
            
        return max_profit

            
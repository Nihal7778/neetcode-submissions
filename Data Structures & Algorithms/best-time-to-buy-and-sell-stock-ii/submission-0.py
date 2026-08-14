class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        total_profit = 0


        for i in range(1,n):

            profit = prices[i] - prices[i-1]

            if profit > 0:

                total_profit+=profit

        return total_profit


        
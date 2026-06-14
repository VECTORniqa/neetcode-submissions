class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxx_profit = 0

        minn_price = prices[0]

        for i in range(len(prices)):
            minn_price = min(prices[i], minn_price)

            profit = prices[i] - minn_price

            maxx_profit = max(profit, maxx_profit)

        return maxx_profit



        
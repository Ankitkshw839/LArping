class Solution(object):
    def maxProfit(self, prices):
        minimum = prices[0]
        maximum_profit = 0

        for price in prices:
            if price < minimum:
                minimum = price
            else:
                profit = price - minimum
                if profit > maximum_profit:
                    maximum_profit = profit

        return maximum_profit
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        buy_price = prices[0]
        for i in range(len(prices)):
            sell_price = prices[i]
            profit = sell_price - buy_price
            if profit < 0:
                buy_price = sell_price
            elif profit > max_profit:
                max_profit = profit
        return max_profit
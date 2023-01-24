class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # buy if stock goes up the next day and you don't currently own a share
        # sell if stock goes down the next day and you currently own a share
        profit = 0
        owned = False

        for i in range(len(prices)-1):
            today_price = prices[i]
            tomorrow_price = prices[i+1]
            if owned and today_price > tomorrow_price:
                profit += today_price - buy_price
                owned = False
            elif not owned and today_price < tomorrow_price:
                buy_price = today_price
                owned = True
        if owned and today_price <= tomorrow_price:
            profit += tomorrow_price - buy_price
        return profit
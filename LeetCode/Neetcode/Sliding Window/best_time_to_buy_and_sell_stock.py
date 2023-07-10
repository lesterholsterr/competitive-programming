class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        # Overall: Sliding window with fairly simple conditions.
        # Leaps
        # - A profit implies the buy date is lower than the sell date. So we keep our buy date the same, and the reverse is true for a loss
        
        # Initial Solution (15 minutes)
        # Yay
        maxsofar = 0
        l = 0
        for r in prices:
            profit = r - prices[l]
            if profit > 0:
                maxsofar = max(maxsofar, profit)
            else:
                while profit < 0:
                    l += 1 # <-- slight optimization, we can actually set l = r!
                    profit = r - prices[l]
        
        return maxsofar
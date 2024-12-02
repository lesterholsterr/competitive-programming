# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

# Initial
# Writing out the "recurrence" to solve an example really helped with deriving the general recurrence
# Completely missed the 2-D aspect though. Solution is O(n^2) when it could be O(n) time
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # f(i) assuming no cooldown
        """
        [1,2,3,0,2] -> 4
        f(0) - answer we want
        f(4) - meaningless because we can't sell
        f(3) = 2. i can buy at t=3, sell at t=4
        f(2) = 2 because i do nothing and use f(3)
        f(1) = 2. I could buy then sell. but then i'm on cooldown at t=3 when I want to buy
        f(0) = 3. Buy, sell, cooldown, buy, sell

        f(0) = max(f(1), f(2), -prices[0] + prices[1] + f(3), -prices[0] + prices[2] + f(4))

        f(i) = max(f(i+1), f(i+2), -prices[i] + prices[i+1] + f(i+3), -prices[i] + prices[i+2] + f(i+4), ...)
        """
        if len(prices) == 1:
            return 0
        elif len(prices) == 2:
            return max(0, -prices[0] + prices[1])
        
        n = len(prices)
        dp = [0] * n
        dp[n-2] = max(0, -prices[n-2] + prices[n-1])
        for i in range(n-3, -1, -1):
            dp[i] = max(0, dp[i+1], dp[i+2])
            for j in range(1, n-i):
                if j < n - i - 2:
                    dp[i] = max(dp[i], -prices[i] + prices[i+j] + dp[i+j+2])
                else:
                    dp[i] = max(dp[i], -prices[i] + prices[i+j]) # <-- missed this case at the start
        return dp[0]

# Optimized time
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # dp[i][0] = at t=i, buy
        # dp[i][1] = at t=i, sell
        n = len(prices)
        dp = [[0, 0] for _ in range(n + 1)]

        for i in range(n-1, -1, -1):
            buy = 0
            if i+1 < n:
                buy = dp[i+1][1] - prices[i]
            buy_cooldown = dp[i+1][0]
            dp[i][0] = max(buy, buy_cooldown)

            sell = prices[i]
            if i+2 < n:
                sell = dp[i+2][0] + prices[i]
            sell_cooldown = dp[i+1][1]
            dp[i][1] = max(sell, sell_cooldown)
        return dp[0][0]

# Optimized space (fucking beautiful)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # dp[0] = at t=i, buy
        # dp[1] = at t=i, sell
        n = len(prices)
        dp, dp1, dp2 = [0, 0], [0, 0], [0, 0]

        for i in range(n-1, -1, -1):
            dp[0] = max(dp1[0], dp1[1] - prices[i])
            dp[1] = max(dp1[1], dp2[0] + prices[i])
            dp, dp1, dp2 = dp2, dp, dp1
        return dp1[0]
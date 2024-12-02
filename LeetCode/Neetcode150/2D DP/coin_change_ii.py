# https://leetcode.com/problems/coin-change-ii/

# Initial - Top down. Still remembered the explanation from this video https://www.youtube.com/watch?v=gK8KmTDtX8E&t=946s
from functools import cache

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        @cache
        def solve(i: int, amt: int) -> int:
            if i == len(coins):
                if amt == 0:
                    return 1
                return 0
            
            if amt - coins[i] >= 0:
                return solve(i+1, amt) + solve(i, amt - coins[i])
            return solve(i+1, amt)
        
        return solve(0, amount)

# Bottom up (the sequel to above video) https://www.youtube.com/watch?v=NA7u5GTh6fw
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # solve(i+1, amt)
        # solve(i, amt - coins[i])
        # if I'm on i, I need i+1. solve bigger first
        # if I'm on amt, I need 0..amt. solve smaller first
        dp = [[0] * (amount + 1) for _ in range(len(coins) + 1)] # <-- Did not initialize properly

        # base case: there's 1 way to make 0 coins
        for i in range(len(coins) + 1): # <-- Did not do this
            dp[i][0] = 1

        for i in range(len(coins) - 1, -1, -1): # <-- Everything below here is good
            for amt in range(amount+1):
                dp[i][amt] = dp[i+1][amt]
                if amt - coins[i] >= 0:
                    dp[i][amt] += dp[i][amt - coins[i]]
        
        return dp[0][amount]


# Space optimized
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [1] + [0] * amount
        dp_next = dp.copy()

        for i in range(len(coins) - 1, -1, -1):
            for amt in range(amount+1):
                dp_next[amt] = dp[amt]
                if amt - coins[i] >= 0:
                    dp_next[amt] += dp_next[amt - coins[i]] # <-- used dp instead of dp_next here. It's i, not i+1!!!
            dp, dp_next = dp_next, dp
        
        return dp[amount] # <-- dp_next is where our answer is. it gets swapped with dp right before this. so return dp

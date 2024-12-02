# thoughts
# - bottom up. I've seen this type of problem before. Just wasn't able to spot the recurrence relation
#   min(1 + dp[amt - coin] for coin in coins)
# - because you have infinite numbers of each coin, you will always have len(coins) choices, which
#   is why the recursive relation contains len(coins) terms

# Initial: backtracking because i can't get the DP solution. TLE of course.
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()

        def dfs(i, n, amount):
            if amount == 0:
                return n
            elif i < 0:
                return -1
            
            if coins[i] <= amount:
                a = dfs(i, n+1, amount-coins[i])
                b = dfs(i-1, n, amount)
                if a == -1 and b == -1:
                    return -1
                elif a == -1:
                    return b
                elif b == -1:
                    return a
                else:
                    return min(a, b)
            else:
                return dfs(i-1, n, amount)
        
        return dfs(len(coins)-1, 0, amount)

# Neetcode solution
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [inf] * (amount+1)
        dp[0] = 0 # <-- important
        # below is unnecessary
        # for c in coins:
        #     if c <= amount:
        #         dp[c] = 1

        for i in range(1, amount+1):
            for c in coins:
                if i-c >= 0:
                    dp[i] = min(1+dp[i-c], dp[i])
        
        return dp[amount] if dp[amount] != inf else -1

# Revisited - forgot the solution but arrived independently at the same thing, nice
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):
            for j in range(len(coins)):
                if i - coins[j] >= 0:
                    dp[i] = min(dp[i], 1 + dp[i - coins[j]])
        return dp[-1] if dp[-1] != float('inf') else -1

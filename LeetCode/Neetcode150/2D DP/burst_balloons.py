# https://leetcode.com/problems/burst-balloons/

# Initial - :(
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        """
        - does greedy work? never pop edge balloons until there's only 2 left. keep popping smallest balloons first.
        - counter: [1, 100, 1] - should pop the edge balloons first
        - but [3, 100, 3] and we actually should pop middle first
        - I don't see a relation. each subproblem feels unique
        - but n can be 300, so it must be DP and not backtracking
        """

# Solution
# Ok I don't feel bad about not being able to solve it anymore
# Intuition:
# - When there are too many subproblems to cache, find a more generalizable subproblem!
# - There's 2^n distinct subsequences, but only n^2 distinct subarrays
# - The biggest leap for me is to ask "what if we pop nums[i] last?"
# - Then you can solve for the most optimal way to pop 2 distinct subarrays, where one of the 
#   edges of the subarray is nums[i]
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]

        @cache
        def dfs(l, r):
            if l > r:
                return 0
            
            max_coins = 0
            for i in range(l, r+1):
                coins = nums[l-1] * nums[i] * nums[r+1]
                coins += dfs(l, i-1) + dfs(i+1, r)
                max_coins = max(max_coins, coins)
            return max_coins
        
        return dfs(1, len(nums) - 2)

# Converting to bottom up for practice
# - First, figure out the loops -> l descending, r ascending is the only way to ensure subproblems have been solved first
# - copy the recurrence from iterative solution
# - modify function calls with dp calls
# - no space saving this time. we need the whole dp matrix.
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        nums = [1] + nums + [1]
        dp = [[0] * (n + 2) for _ in range(n+2)]

        for l in range(n, 0, -1):
            for r in range(l, n + 1):
                for i in range(l, r + 1):
                    coins = nums[l - 1] * nums[i] * nums[r+1]
                    coins += dp[l][i - 1] + dp[i + 1][r]
                    dp[l][r] = max(dp[l][r], coins)
        
        return dp[1][n]

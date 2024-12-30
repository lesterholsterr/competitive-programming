# https://leetcode.com/problems/distinct-subsequences/description/

# Initial - took a while to find the recurrence, but I think the thought process was good
# bottom-up + space saving on the first attempt :sunglasses:
# the intuition for the recurrence was similar to coin change (take vs skip)
# can actually do this without the dp_next array. too lazy to redo though
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        """
        obviously we need to look for appearences of t[0] in s
        if s[i] = t[0], then we need to know f(i+1, 1) = # of ways to make t[1:] using s[i+1:]
        base case: f(len(s), len(t)) = 1 (we can make nothing using nothing)
        both params decrease. 1st one should be the "outer" loop. we only need the i+1'th row to get the i'th row

        ^NOPE - actually 2nd should be outer loop. We need j+1 to get j.
        """
        dp = [1] * (len(s) + 1) # base case: I can always make the empty string
        for i in range(len(t) - 1, -1, -1):
            dp_next = [0] * (len(s) + 1)
            for j in range(len(s) - 1, -1, -1):
                if s[j] == t[i]:
                    dp_next[j] = dp[j+1] + dp_next[j+1] # <-- recurrence
                else:
                    dp_next[j] = dp_next[j+1]
            dp = dp_next
        return dp[0]

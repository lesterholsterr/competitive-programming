# https://leetcode.com/problems/edit-distance/description/
# - Feel like this one should be labelled hard and distinct subsequences should be easy
# - This is like the subsequence problem, except there are 4 choices instead of 2
# - When there's >2 choices, drawing a decision tree might help intuit the recurrence

# Initial - thought this would work, but actually it doesn't
# problem is that we also need to account for the position of each character in the LCS in each string...
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        one solution would be
        - find longest common subsequence
        - return len(word1) - len(LCS)
        
        LCS
        - f(i, j) = len(LCS) for word1[i:] and word2[j:]
                  = max(f(i+1, j), f(i, j+1)) or 1 + f(i+1, j+1) if word1[i] == word2[j]
        - shouldn't matter which loop is outer vs inner. both descending.
        """
        def lcs(s1, s2) -> int:
            dp = [0] * (len(s2) + 1)
            for i in range(len(s1) - 1, -1, -1):
                dp_next = dp.copy()
                for j in range(len(s2) - 1, -1, -1):
                    dp_next[j] = max(dp[j], dp_next[j+1])
                    if s1[i] == s2[j]:
                        dp_next[j] = max(dp_next[j], 1 + dp[j+1])
                dp = dp_next
            return dp[0]
        
        return len(word1) - lcs(word1, word2)

# Solution + intuition below
# don't forget to consider edge cases before submitting next time.
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        f(i, j) = # ops to convert word1[i:] to word2[j:]
        - insert: 1 + f(i, j+1)
        - delete: 1 + f(i+1, j)
        - swap:   1 + f(i+1, j+1)
        - word1[i] == word2[j]: f(i+1, j+1)
        """
        if len(word1) < len(word2): # <-- missed this edge case
            word1, word2 = word2, word1
        
        dp = []
        for i in range(len(word1), -1, -1):
            dp.append(i) # <-- unique looking base case
        
        for i in range(len(word2) - 1, -1, -1):
            dp_next = dp.copy()
            dp_next[-1] = len(word2) - i # <-- missed this edge case
            for j in range(len(word1) - 1, -1, -1):
                if word2[i] == word1[j]:
                    dp_next[j] = dp[j+1]
                else:
                    dp_next[j] = 1 + min(dp_next[j+1], dp[j], dp[j+1])
            dp = dp_next
        return dp[0]

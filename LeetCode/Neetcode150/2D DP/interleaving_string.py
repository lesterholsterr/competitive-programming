# https://leetcode.com/problems/interleaving-string/description/

# Initial - works, but pretty bad. Also some observations are not true.
# There's no need for k because k = i+j
# There's no need for l because just do DFS and 2 recursive calls
# Therefore there are only 1e4 possibilities to cahce
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        """
        observations
        - example 2 not possible because no 'a's after first 'c'
        - f(i, j, k, 0/1) - given s1[i:] and s2[j:], can we make s3[k:] starting from s1? starting from s2?
        - 100 * 100 * 200 = 2e6 possibilities to cache
        - bottom-up? base case is f(len(s1), len(s2), k) = 1
        """

        @cache
        def dp(i: int, j: int, k: int, l: bool) -> bool:
            if i == len(s1) and j == len(s2) and k == len(s3):
                return True
            elif l:
                # start with s1
                for x in range(1, len(s1) - i + 1):
                    if s1[i : i + x] == s3[k : k + x]:
                        if dp(i + x, j, k + x, False):
                            return True
                    else:
                        break
            else:
                # start with s2
                for x in range(1, len(s2) - j + 1):
                    if s2[j : j + x] == s3[k : k + x]:
                        if dp(i, j + x, k + x, True):
                            return True
                    else:
                        break
            return False

        return dp(0, 0, 0, True) or dp(0, 0, 0, False)

# Optimized top-down
# Already much faster, but of course we can do better on memory...
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        
        @cache
        def dfs(i: int, j: int) -> bool:
            if i == len(s1) and j == len(s2):
                return True
            
            res = False
            if i != len(s1) and s1[i] == s3[i+j]:
                res = dfs(i+1, j)
            if j != len(s2) and s2[j] == s3[i+j]:
                res = res or dfs(i, j+1)

            return res

        return dfs(0, 0)

# Bottom-up. Makes sense, just need more practice to code this solution FASTER
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        if len(s1) < len(s2):
            s1, s2 = s2, s1

        dp = [False] * len(s2) + [True]
        for i in range(len(s1), -1, -1):
            for j in range(len(s2), -1, -1):
                if i < len(s1) and dp[j] and s1[i] == s3[i+j]:
                    dp[j] = True
                elif j < len(s2) and dp[j+1] and s2[j] == s3[i+j]:
                    dp[j] = True
                elif i == len(s1) and j == len(s2): # <-- missed the base case :|
                    dp[j] = True
                else:
                    dp[j] = False
        return dp[0]

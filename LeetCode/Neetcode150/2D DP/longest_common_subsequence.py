# Very good editorial explanation
# - Start with recursion: If I'm at index i in text1 and index j in text2, I can make a greedy decision, or 'skip' one of these characters
# - Ok now write that with memoization (fairly straightforward)
# - Now we look for a bottom up solution... notice that there is 1 case where greedy always works:
#   - If text1[i] == text2[j], always take that match -> 1 + LCS(i+1, j+1)
#   - Otherwise, the solution is the better of LCS(i+1, j) and LCS(i, j+1)
# - So if I'm at (i, j), I only need the answers to (i+1, j+1), (i+1, j), and (i, j+1)
# - (HERE IS THE MENTAL LEAP ->) Therefore you can start from the bottom right of the DP matrix and go from bottom to top, and right to left!!!
# - Also you don't need a matrix since you only ever use 2 columns

# Initial (top down)
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[-1] * n for _ in range(m)]

        def LCS(i : int, j : int) -> int:
            if i == m or j == n:
                return 0
            elif dp[i][j] != -1:
                return dp[i][j]

            c = text1[i]
            k = j
            while k < n:
                if text2[k] == c:
                    break
                k += 1
            
            if k < n:
                dp[i][j] = max(LCS(i+1, j), 1 + LCS(i+1, k+1))
            else:
                dp[i][j] = LCS(i+1, j)
            return dp[i][j]

        return LCS(0, 0)

# Better (bottom up)
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0] * (n+1) for _ in range(m+1)]

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = dp[i+1][j+1] + 1
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])
        return dp[0][0]

# Even better (space optimized)
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        prev = [0] * (n+1)
        cur = prev.copy()

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if text1[i] == text2[j]:
                    cur[j] = prev[j+1] + 1
                else:
                    cur[j] = max(prev[j], cur[j+1])
            prev, cur = cur, prev
        
        return prev[0]

# Overall: I'm actually so big brain
# Already familiar with the recursive definition of a palindrome, the DP just came naturally this time.
# Still don't have a good knack for DP problems though. Solutions are always obvious in hindsight.

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        l = len(s)
        dp = [[0] * l for _ in range(l)]
        
        for i in range(l):
            # every letter is a palindrome
            dp[i][i] = 1

            # double letters are palindromes
            if i != l-1 and s[i] == s[i+1]:
                dp[i][i+1] = 1

        # X<palindrome>X is a palindrome
        for x in range(2, l):
            for i in range(0, l-x):
                if s[i] == s[i+x] and dp[i+1][i+x-1] == 1:
                    dp[i][i+x] = 1
        
        ans = []
        cur = []
        def bt(i):
            if i == l:
                ans.append(cur[:])
                return
            for x in range(i, l):
                if dp[i][x] == 1:
                    cur.append(s[i:x+1])
                    bt(x+1)
                    cur.pop()
        
        bt(0)
        return ans
# https://leetcode.com/problems/regular-expression-matching/description/

# Initial - I did it!
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """
        first thought is 2 pointers - match s[i] with p[j]
        the hard part is knowing how many to match when you see a Kleene star
        there are a finite amount of choices though, so we can cache subproblems
        - let f(i, j) = s[i:] matches p[j:]
        - base case: f(len(s), len(p)) = True
        - if s[i] == p[j] or p[j] == '.', then f(i+1, j+1)
        - BUT if p[j+1] == '*', then f(i+k, j+2) for k in 1..len(s)-i
        """
        l, m = len(s), len(p)
        
        @cache
        def dfs(i, j) -> bool:
            if i == l and j == m:
                return True
            elif j + 1 < m and p[j + 1] == '*':
                for k in range(l - i + 1): # <-- for loop is redundant! handling * is just a take/skip decision (increment i by 1, or j by 2)
                    if k == 0 or p[j] == '.' or s[i + k - 1] == p[j]:
                        if dfs(i + k, j + 2):
                            return True
                    else:
                        break
            elif i == l or j == m: # <-- Need to put this case AFTER checking '*' because of cases like s = "a", p = "ab*"
                return False
            elif s[i] == p[j] or p[j] == '.':
                return dfs(i+1, j+1)
            return False
        
        return dfs(0, 0)

# Neetcode - same idea, more elegant impl
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        l, m = len(s), len(p)
        
        @cache
        def dfs(i, j) -> bool:
            if j == m:
                return i == l
            
            match = i < l and (s[i] == p[j] or p[j] == '.')
            if j + 1 < m and p[j + 1] == '*':
                return (match and dfs(i + 1, j)) or dfs(i, j + 2)
            elif match:
                return dfs(i + 1, j + 1)
            return False
        
        return dfs(0, 0)

# Bottom-up
# Maybe for another day :P

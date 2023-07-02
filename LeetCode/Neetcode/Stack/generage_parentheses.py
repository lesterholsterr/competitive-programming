class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        # Overall: Look for patterns/rules in the output to come up with recursive cases for a backtracking algorithm.
        # Leaps
        # - What do we know? 
        #   - There must be n '('s and n ')'s. 
        #   - At any given moment, there must be more '(' than ')', or an equal amount.
        # - As long as we follow the above 2 rules, we know a string is valid if open == close == n

        # Initial Approach (15 mins)
        # No idea what I was doing here...
        res = []
        s = ""
        for i in range(1, n, 1):
            s = ""
            for j in range(i):
                s += "()"
            for k in range(n-i):
        
        # Neetcode Solution
        res = []

        def addParentheses(open, close, s):
            if open == close and close == n:
                res.append(s)
                return
            if open < n:
                s1 = s + "("
                addParentheses(open+1, close, s1)
            if close < open:
                s2 = s + ")"
                addParentheses(open, close+1, s2)

        addParentheses(0, 0, "")
        return res
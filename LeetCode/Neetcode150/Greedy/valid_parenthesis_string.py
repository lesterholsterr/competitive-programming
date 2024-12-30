# https://leetcode.com/problems/valid-parenthesis-string/
# Problem lends itself to a decision tree -> DP
# But we can do even better with a greedy solution...
# Will definitely have to revisit... took me a very long time to understand the intuition here

# Initial - fails a big test case
# The problem here is abs(balance) <= wildcards doesn't account for positioning of course
class Solution:
    def checkValidString(self, s: str) -> bool:
        # ( - balance + 1
        # ) - balance - 1
        # * - wildcards + 1
        # balance > 0 is okay because they might get closed off later...
        # balance < 0 is more serious. we need to "cancel them out" with wildcards
        balance = 0
        wildcards = 0
        for c in s:
            if c == '(':
                balance += 1
            elif c == ')':
                balance -= 1
            else:
                wildcards += 1
            
            if balance < 0:
                if wildcards > 0:
                    balance += 1
                    wildcards -= 1
                else:
                    return False
        
        return abs(balance) <= wildcards

# Optimal - I never would have figured this out...
# bal_max = turn every * into a (. If this ever goes negative, we are dunzo
# bal_min = turn every * into a )... BUT we can reset this value to 0 anytime it goes negative
#           we can do this because * can always be NOTHING. If we do this too many times,
#           then bal_max will go negative, so we will find out anyways
class Solution:
    def checkValidString(self, s: str) -> bool:
        bal_min, bal_max = 0, 0
        for c in s:
            if c == '(':
                bal_min += 1
                bal_max += 1
            elif c == ')':
                bal_min -= 1
                bal_max -= 1
            else:
                bal_min -= 1
                bal_max += 1
            
            if bal_max < 0:
                return False
            if bal_min < 0:
                bal_min = 0

        return bal_min == 0

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        # Overall: Be cognisant of all 3 rules, and won't miss any edge cases
        # Leaps: Not much... quite obviously a stack problem.

        # Initial Solution (15 mins)
        pairs = {'(': ')', '[': ']', '{': '}'}
        stack = []
        for p in s:
            if p in pairs:
                stack.append(p)
            elif len(stack) == 0:
                return False
            else:
                last_p = stack.pop()  # <-- Problem was I didn't put this in an else block!
                expected_p = pairs[last_p]
                if expected_p != p:
                    return False

        if len(stack) == 0:
            return True
        return False

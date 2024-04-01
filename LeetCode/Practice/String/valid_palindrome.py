class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        f = 0
        b = len(s) - 1
        while f < b:
            if not s[f].isalnum():
                f += 1
            elif not s[b].isalnum():
                b -= 1
            elif s[f] != s[b]:
                return False
            else:
                f += 1
                b -= 1
        return True
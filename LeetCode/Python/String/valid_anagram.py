class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t): return False

        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        for letter in alphabet:
            if s.count(letter) != t.count(letter):
                return False
        return True
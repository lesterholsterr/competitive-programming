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

# Alternate Solution
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        letters = {}
        for c in s:
            if c in letters:
                letters[c] += 1
            else:
                letters[c] = 1
        for c in t:
            if c in letters:
                if letters[c] == 0:
                    return False
                else:
                    letters[c] -= 1
            else:
                return False
        for c in s:
            if letters[c] != 0:
                return False
        return True
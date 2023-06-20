class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        # Overall: Cheeky solution
        # Syntax: s.count(l) returns the number of times l appears in string s
        # Leaps
        # - Two words are anagrams if each letter appears the same number of times

        alphabet = "abcdefghijklmnopqrstuvwxyz"
        for letter in alphabet:
            if s.count(letter) != t.count(letter):
                return False
        return True


class Solution2(object):
    def isAnagram2(self, s, t):
        # Much longer solution
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

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        pal_length = 0
        letters = {}
        middle_letter = True

        for c in s:
            if c in letters:
                letters[c] += 1
            else:
                letters[c] = 1
        
        for letter in letters:
            if letters[letter] % 2 == 0:
                pal_length += letters[letter]
            elif middle_letter:
                pal_length += letters[letter]
                middle_letter = False
            else:
                pal_length += letters[letter] - 1
        return pal_length
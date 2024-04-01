class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        mag_letters = {}
        for letter in magazine:
            if letter in mag_letters:
                mag_letters[letter] += 1
            else:
                mag_letters[letter] = 1
        for letter in ransomNote:
            if letter in mag_letters:
                if mag_letters[letter] == 0:
                    return False
                else: 
                    mag_letters[letter] -= 1
            else:
                return False
        return True
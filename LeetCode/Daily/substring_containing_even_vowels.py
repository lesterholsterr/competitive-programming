# 1371. Find the Longest Substring Containing Vowels in Even Counts
# New tool in the toolkit: bitmasking
# - Assign each vowel a power of 2
# - XOR the vowels to get a unique number for each combination of parity of vowels (e.g. even a's, odd e's, ...)
# - Store the index of the first occurrence of each unique number (<-- not intuitive to me)
# - LEAP: If the same number is encountered again, the substring between the first occurrence and the current occurrence MUST have even counts of each vowel

class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        vowels = {'a': 1, 'e': 2, 'i': 4, 'o': 8, 'u': 16}
        first_occurrence = {0: -1}

        mask = 0
        max_len = 0

        for i in range(len(s)):
            c = s[i]
            if c in vowels:
                mask ^= vowels[c]
            
            if mask in first_occurrence:
                max_len = max(max_len, i - first_occurrence[mask])
            else:
                first_occurrence[mask] = i
        
        return max_len
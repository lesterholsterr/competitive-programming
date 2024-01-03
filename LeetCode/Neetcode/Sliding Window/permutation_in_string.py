class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        # Overall:
        # - Intuitive application of sliding window for an anagram. Otherwise, there really was no strategy other than just "find the algorithm"

        # Initial Solution (25 minutes)
        # Time: O(n), sliding window argument
        # This looks disgusting but it works
        freq = {}
        for c in s1:
            if c in freq:
                freq[c] += 1
            else:
                freq[c] = 1
        
        l = r = 0
        while r < len(s2):
            c = s2[r]
            if c in freq and freq[c] == 0:
                # Move l over 1 by 1 until we find the next appearance of c
                while s2[l] != c:
                    if s2[l] in freq:
                        freq[s2[l]] += 1
                    l += 1
                # Then move it one more time to skip over this duplicate
                l += 1
            elif c in freq:
                freq[c] -= 1
            else:
                # Bring left all the way over to right
                while l != r:
                    if s2[l] in freq:
                        freq[s2[l]] += 1
                    l += 1
            
            # Permutation iff we exactly used up all the letters in s1 (so freq is empty)
            if sum(freq.values()) == 0:
                return True
            else:
                r += 1
        
        return False

        # NeetCode Solution
        # Also not very elegant. I honestly like my solution better.
        if len(s1) > len(s2):
            return False
        
        s1Count, s2Count = [0] * 26, [0] * 26
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord("a")] += 1
            s2Count[ord(s2[i]) - ord("a")] += 1

        matches = 0
        for i in range(26):
            if s1Count[i] == s2Count[i]: matches += 1
        
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            
            index = ord(s2[r]) - ord("a")
            s2Count[index] += 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1
            
            index = ord(s2[l]) - ord("a")
            s2Count[index] -= 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1
            l += 1
        return matches == 26
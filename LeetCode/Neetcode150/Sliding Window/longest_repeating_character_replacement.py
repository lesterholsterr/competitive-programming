class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """

        # Overall: The motivation behind sliding window is we only have to slide through the string/list ONCE. The tough part is finding a sufficient condition to allow us to do this.
        # Leaps
        # - For any given substring, how can we find the minimum number of replacements to make the substring contain only 1 character? (len(substr) - count of most frequent char)
        # - Which letter we are replacing with is a red herring. We only care about how many letters NEED replacing. This leads us to a frequency dictionary.

        # Initial Solution (30 minutes)
        # Very unpleasant brute force, I think it works but times out on Testcase 23.
        # Not sure how to turn into a more efficient sliding window
        letters = set()
        for c in s:
            if c not in letters:
                letters.add(c)

        maxsofar = 0
        for c in letters:
            cur = 0
            changes = 0
            l = 0
            r = 0
            while l < len(s):
                while r < len(s):
                    if s[r] != c and changes < k:
                        changes += 1
                    elif s[r] != c and changes == k:
                        break
                    r += 1
                    cur += 1
                    maxsofar = max(maxsofar, cur)
                l += 1
                r = l
                cur = 0
                changes = 0
        return maxsofar

        # Neetcode Soluiton
        l = 0
        maxsofar = 0
        freq = {}

        # As with the last sliding window problem, we can use r as the for loop iterator rather manually controlling it
        for r in range(len(s)):
            freq[s[r]] = 1 + freq.get(s[r], 0)

            if r - l + 1 - max(freq.values()) > k: # Clever validity rule
                freq[s[l]] -= 1
                l += 1
            
            maxsofar = max(maxsofar, r - l + 1)
        return maxsofar
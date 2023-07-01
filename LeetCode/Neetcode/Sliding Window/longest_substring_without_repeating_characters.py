class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        # Overall:
        # Leaps
        # - Start from brute force and the intuitive optimization leads to a 2-pointer approach
        # - How can we represent a substring to check dupes in a time-efficient way? (set)

        # Initial Solution (15 minutes)
        # Time: O(n^2), I think
        curlen = 0
        maxsofar = 0
        seen = set()

        for i in range(len(s)):
            if s[i] in seen:
                curlen = 1
                seen.clear()
                seen.add(s[i])
                for j in range(i - 1, -1, -1):
                    if s[j] == s[i]:
                        break
                    else:
                        seen.add(s[j])
                        curlen += 1
            else:
                seen.add(s[i])
                curlen += 1

            maxsofar = max(maxsofar, curlen)

        return maxsofar

        # Neetcode Solution
        maxsofar = 0
        seen = set()
        l = 0

        # Instead of manually incrementing r, just make it the for loop iterator!
        for r in range(len(s)):
            while s[r] in seen:  # Creative while loop condition removes edge case handling!
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            maxsofar = max(maxsofar, r - l + 1)

        return maxsofar

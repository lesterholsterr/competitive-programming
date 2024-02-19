class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        # Overall: Many valid solutions. Most efficient one requires out of the box thinking.
        # Also note that dictionary keys cannot be lists, hence we cast them to tuples.
        # Leaps
        # - How can we represent can we represent words in such a way that comparing whether two words are anagrams can be done in O(1)?
        #     - Comparison in O(1) suggests hashing
        #     - Representation is a frequency list of length 26, with each letter of the alphabet implicitly mapped to an index!

        res = {}
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            
            if tuple(count) in res:
                res[tuple(count)].append(s)
            else:
                res[tuple(count)] = [s]
        return res.values()
from collections import defaultdict

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # Solution copied from https://www.youtube.com/watch?time_continue=469&v=vzdNOK2oB2E&embeds_euri=https%3A%2F%2Fneetcode.io%2F&source_ve_path=MjM4NTE&feature=emb_title
        
        res = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c)-ord('a')] += 1
            res[tuple(count)].append(s)

        return res.values()

        # Less cool but more efficient solution
        # From https://leetcode.com/problems/group-anagrams/solutions/2384037/python-easily-understood-hash-table-fast-simple/

        res = {}

        for s in strs:
            letters = ''.join(sorted(s))
            if letters in res:
                res[letters].append(s)
            else:
                res[letters] = [s]

        return res.values()
        
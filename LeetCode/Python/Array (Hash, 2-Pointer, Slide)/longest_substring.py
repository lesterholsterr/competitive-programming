class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen = set()
        max_substr = 0
        start = 0
        cur = 0

        while cur < len(s):
            if s[cur] in seen:
                seen.remove(s[start])
                start += 1
            else:
                seen.add(s[cur])
                max_substr = max(max_substr, cur-start+1)
                cur += 1
        return max_substr
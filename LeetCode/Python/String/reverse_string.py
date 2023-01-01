class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        l = len(s)
        if l % 2 == 0:
            mid = l/2
        else: mid = round(l/2) + 1
        for i in range(int(mid)):
            s[i], s[l-1-i] = s[l-1-i], s[i]
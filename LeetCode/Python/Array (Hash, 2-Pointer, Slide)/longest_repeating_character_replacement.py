class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        s_lst = list(s)
        k_remaining = k
        max_sub = 0
        cur_sub = 0
        cur_char = ''
        index = 0

        for i, c in enumerate(s_lst):
            k_remaining = k
            cur_char = c
            index = i
            cur_sub = 1
            while i < len(s_lst)-1:
                i += 1
                if s_lst[i] != cur_char and k_remaining > 0:
                    k_remaining -= 1
                elif s_lst[i] != cur_char and k_remaining == 0:
                    break
                cur_sub += 1
            if cur_sub > max_sub:
                max_sub = cur_sub
        
        return max_sub
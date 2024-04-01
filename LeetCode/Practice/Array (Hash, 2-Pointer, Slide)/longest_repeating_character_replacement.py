class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """

        # Attempt 1 (very proud of this, got quite close)
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

        # Attempt 2
        # Solution from: https://www.youtube.com/watch?time_continue=198&v=gqXU1UyA8pk&embeds_euri=https%3A%2F%2Fneetcode.io%2F&source_ve_path=MjM4NTE&feature=emb_title
        count = {}
        res = 0
        l = 0

        for r in range(len(s)):
            if s[r] in count:
                count[s[r]] += 1
            else:
                count[s[r]] = 1

            if r-l+1 - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r-l+1)
        
        return res
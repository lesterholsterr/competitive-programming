# Overall:

# Initial Solution
# Time: O(m^2). Timed out on the 3rd last case D:
class Solution:
    def minWindow(self, s: str, t: str) -> str:

        def freqlist(s):
            fl = [0] * 58
            for c in s:
                fl[ord(c) - ord('A')] += 1
            return fl

        ans = ""
        l, r = 0, 0
        ft = freqlist(t)

        while r < len(s):
            ss = s[l:r+1]
            fss = freqlist(ss)

            valid = True
            for i in range(len(fss)):
                if fss[i] < ft[i]:
                    valid = False
                    break
            if valid:
                if ans == "":
                    ans = ss
                elif len(ans) > len(ss):
                    ans = ss
                l += 1
            else:
                r += 1

        return ans

# Second Attempt
# Time: O(m + n) in theory
# But now instead of timing out, I'm getting a wrong answer for that super big case
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ans = ""
        ft, fs = {}, {}
        for c in t:
            if c not in ft:
                ft[c] = 1
                fs[c] = 0
            else:
                ft[c] += 1

        have, need = 0, len(ft)
        l = 0
        for r in range(len(s)):
            if s[r] in fs:
                fs[s[r]] += 1
                if fs[s[r]] == ft[s[r]]:
                    have += 1
            while have == need:
                if ans == "" or l-r+1 < len(ans): # bruh the mistake was r-l+1 instead 💀
                    ans = s[l:r+1]
                if s[l] in fs:
                    fs[s[l]] -= 1
                    if fs[s[l]] == ft[s[l]] - 1:
                        have -= 1
                l += 1

        return ans


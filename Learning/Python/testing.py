def minWindow(s: str, t: str) -> str:
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
            if ans == "" or l-r+1 < len(ans):
                ans = s[l:r+1]
            if s[l] in fs:
                fs[s[l]] -= 1
                if fs[s[l]] == ft[s[l]] - 1:
                    have -= 1
            l += 1
    
    return ans

print(minWindow("cabwefgewcwaefgcf", "cae"))
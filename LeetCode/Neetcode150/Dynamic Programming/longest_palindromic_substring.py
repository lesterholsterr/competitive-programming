# Overall: Yeah I got skill gapped. Notice that the brute force time complexity is actually O(n^3).
# So even making it O(n^2) is good. Either make O(n) comparisons, or check palindrome in O(1)
# The latter doesn't seem doable. So instead observe that the longest palindrome's middle letter(s)
# must be one (two) of the given letters. Now we have O(n) comparisons and O(n) checking time.
# The case of the palindrome having an even length is a 'reduce to previously solved problem'

# Initial Solution: I got nothing but brute force :(

# Neetcode Solution
class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ""

        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r-l+1 > len(ans):
                    ans = s[l:r+1]
                l -= 1
                r += 1

            l, r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r-l+1 > len(ans):
                    ans = s[l:r+1]
                l -= 1
                r += 1
            
        return ans

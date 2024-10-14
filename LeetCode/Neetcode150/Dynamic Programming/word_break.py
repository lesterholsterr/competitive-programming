# Thoughts: parody of coin change, bottom up iterative. Nothing special.

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[0] = True  # Base case: an empty string can always be segmented
        valid_words = set(wordDict)

        for i in range(len(s) + 1):
            if dp[i]:
                for word in valid_words:
                    if i + len(word) <= len(s) and s[i:i + len(word)] == word:
                        dp[i + len(word)] = True

        return dp[len(s)]
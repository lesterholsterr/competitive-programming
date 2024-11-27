# https://leetcode.com/problems/longest-increasing-subsequence/

# Was able to figure out what the various "states" of the DP array represent
# Needed some help to see the "strong induction" recurrence
# For the future: Try and find a recurrence relation no matter how many previous
#   states you have to use...
# Also going directly to bottom up was pretty straightforward here
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # [10,9,2,5,3,7,101,18]
        # Consider nums[i]
        # I should know the longest subsequence for nums[i-1], nums[i-1],... nums[0]
        # I should know the largest number in each subsequence -> it's simply nums[i-j]!
        # if nums[i] > nums[i-j], then dp[i] can be a subsequence of length dp[i-j] + 1 
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

# The O(nlogn) solution is fucking witchcraft I would never come up with in a million years

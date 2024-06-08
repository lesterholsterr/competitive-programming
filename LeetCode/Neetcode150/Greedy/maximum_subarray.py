# Not much to say, basically just sliding window
# So this is labelled as a "greedy" problem I guess
# - Make LOCALLY optimal choices at each step in the hopes of finding a GLOBALLY optimal solution.
# - No backtracking (don't reconsider your choices)
# - Fast and simple, might not explore all possibilities.
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur, maxsofar = nums[0], nums[0]
        for i in range(1, len(nums)):
            if nums[i] > cur+nums[i]:
                cur = nums[i]
            else:
                cur += nums[i]
            maxsofar = max(cur, maxsofar)
        return maxsofar
